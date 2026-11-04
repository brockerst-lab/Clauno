"""Minimal source-dependent master: 20 Hz subsonic HPF + gain to target LUFS, TP ceiling check."""
import sys, numpy as np, soundfile as sf, pyloudnorm as pyln
from scipy.signal import butter, sosfiltfilt, resample_poly
src, dst, target = sys.argv[1], sys.argv[2], float(sys.argv[3])
x, sr = sf.read(src, always_2d=True)
sos = butter(2, 20, btype='highpass', fs=sr, output='sos')
y = sosfiltfilt(sos, x, axis=0)              # zero-phase, preserves transients
I = pyln.Meter(sr).integrated_loudness(y)
g = 10**((target - I)/20)
y *= g
tp = 20*np.log10(np.max(np.abs(resample_poly(y, 4, 1, axis=0))))
assert tp <= -1.0, f"true peak {tp:.2f} dBTP exceeds -1 ceiling; limiter needed"
sf.write(dst, y, sr, subtype='PCM_24')
print(f"gain {20*np.log10(g):+.2f} dB, true peak {tp:.2f} dBTP")
