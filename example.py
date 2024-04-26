from morph1D import morph
import numpy as np
import proplot as pplt

x = np.array(
    [
        0.0,
        0.0413,
        0.0945,
        0.1245,
        0.1478,
        0.1772,
        0.1983,
        0.201,
        0.23,
        0.2543,
        0.3076,
        0.3608,
        0.4141,
        0.4674,
        0.5206,
        0.5739,
        0.6272,
        0.6804,
        0.7337,
        0.7869,
        0.8402,
        0.8935,
        0.9467,
        0.9684,
        0.9789,
        1.0,
    ]
)
y = np.array(
    [
        0.0144,
        0.0209,
        0.026,
        0.0287,
        0.0304,
        0.0316,
        0.0318,
        0.0318,
        0.0312,
        0.0304,
        0.0284,
        0.0263,
        0.0244,
        0.0225,
        0.0208,
        0.0195,
        0.0179,
        0.0165,
        0.0153,
        0.0143,
        0.0134,
        0.0123,
        0.0114,
        0.0107,
        0.01,
        0.0059,
    ]
)

n_points = 4
# dy = np.random.rand(n_points) * 0.02 - 0.01
dy = np.random.rand(n_points) * 0.4 - 0.2

_, y_morphed = morph(x, y, dy, relative=True)


fig, ax = pplt.subplots(figsize=(4,3))
ax.plot(x, y, label="original")
ax.plot(x, y_morphed, label="morphed")
ax.set(xlabel="x", ylabel="y")
ax.legend()
# fig.savefig("example.png", dpi=300)
pplt.show()