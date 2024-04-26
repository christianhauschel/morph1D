from pygem import RBF
import numpy as np


def morph(
    x: np.array,
    y: np.array,
    dy: np.array,
    relative=False,
    func="gaussian_spline",
    radius=0.5,
    extra=None,
) -> tuple:
    """Morphes the shape of a 1D curve using RBF.

    Parameters
    ----------
    x : np.array
        points of the curve
    y : np.array
        points of the curve
    dy : np.array
        Specifies by which amount the curve should be morphed.
    relative : bool, optional
        Morph by dy relatively or absolutly, by default False
    func : str, optional
        RBF function, by default "gaussian_spline"
    radius : float, optional
        RBF radius, by default 0.5
    extra : _type_, optional
        extra params for RBF, by default None

    Returns
    -------
    tuple
        x_deformed : np.array
        y_deformed : np.array
    """

    n_points = len(dy)

    x_points = np.linspace(0, 1, n_points)
    y_points = np.interp(x_points, x, y)
    z_points = np.zeros_like(x_points)
    z_points[n_points - 1 :] = 1.0

    if relative:
        dy *= y_points

    control_points = np.array([x_points, y_points, z_points]).T
    deformed_points = np.array([x_points, y_points + dy, z_points]).T

    rbf = RBF(
        original_control_points=control_points,
        deformed_control_points=deformed_points,
        func=func,
        radius=radius,
        extra_parameter=extra,
    )

    mesh = np.array([x, y, np.zeros_like(x)]).T
    deformed_mesh = rbf(mesh)

    x_deformed = deformed_mesh[:, 0]
    y_deformed = deformed_mesh[:, 1]

    return x_deformed, y_deformed
