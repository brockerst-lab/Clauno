"""Measure a stereo audio file: format, loudness, true peak, LRA, spectrum balance, stereo."""
import sys, json, subprocess
import numpy as np, soundfile as sf, pyloudnorm as pyln
from scipy.signal import resample_poly, butter, sosfilt

def true_peak_db(x, sr):
    up = resample_poly(x, 4, 1, axis=0)
    return 20*np.log10(np.max(np.abs(up))+1e-12)

def band_share(m, sr):
    bands = {"sub <60":(20,60),"low 60-250":(60,250),"lowmid 250-2k":(250,2000),
             "presence 2k-6k":(2000,6000),"air 6k-16k":(6000,16000)}
    out = {}
    tot = np.mean(m**2)+1e-20
    for k,(lo,hi) in bands.items():
        sos = butter(4,[lo,min(hi,sr/2-100)],btype='band',fs=sr,output='sos')
        out[k] = round(10*np.log10(np.mean(sosfilt(sos,m)**2)/tot+1e-20),1)
    return out

def measure(path):
    info = sf.info(path)
    x, sr = sf.read(path, always_2d=True)
    meter = pyln.Meter(sr)
    I = meter.integrated_loudness(x)
    # short-term (3 s) loudness series
    hop, win = sr, 3*sr
    st = [meter.integrated_loudness(x[i:i+win]) for i in range(0, len(x)-win, hop)]
    st = np.array([s for s in st if np.isfinite(s) and s > -70])
    lra = float(np.percentile(st,95)-np.percentile(st,10)) if len(st) else None
    L, R = x[:,0], x[:,1] if x.shape[1] > 1 else x[:,0]
    corr = float(np.corrcoef(L,R)[0,1])
    side = (L-R)/2; mid = (L+R)/2
    clip = int(np.sum(np.abs(x) >= 0.9999))
    return {
      "file": path, "format": info.format, "subtype": info.subtype, "sr": sr,
      "channels": info.channels, "duration_s": round(info.duration,2),
      "integrated_LUFS": round(I,2), "true_peak_dBTP": round(true_peak_db(x,sr),2),
      "sample_peak_dBFS": round(20*np.log10(np.max(np.abs(x))+1e-12),2),
      "LRA_approx_LU": round(lra,1) if lra is not None else None,
      "short_term_max_LUFS": round(float(st.max()),1), "short_term_min_LUFS": round(float(st.min()),1),
      "crest_dB": round(20*np.log10(np.max(np.abs(x))/np.sqrt(np.mean(x**2))),1),
      "LR_correlation": round(corr,3),
      "side_to_mid_dB": round(10*np.log10(np.mean(side**2)/np.mean(mid**2)+1e-20),1),
      "LR_balance_dB": round(10*np.log10(np.mean(L**2)/np.mean(R**2)),2),
      "clipped_samples": clip,
      "band_energy_dB_rel_total": band_share(mid, sr),
    }

if __name__ == "__main__":
    print(json.dumps([measure(p) for p in sys.argv[1:]], indent=1))
