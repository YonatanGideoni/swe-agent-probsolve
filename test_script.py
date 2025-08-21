from pack_circ import pack_circles
import numpy as np

def is_valid(centers: np.ndarray, radii: np.ndarray) -> bool:
    """Checks if the packing is valid (no overlaps, inside the square)."""
    for i in range(len(radii)):
        # Check if circle is inside the square
        if (centers[i, 0] - radii[i] < 0 or centers[i, 0] + radii[i] > 1 or
            centers[i, 1] - radii[i] < 0 or centers[i, 1] + radii[i] > 1):
            return False
        # Check for overlaps
        for j in range(i + 1, len(radii)):
            dist = np.linalg.norm(centers[i] - centers[j])
            if dist < radii[i] + radii[j]:
                return False
    return True


if __name__ == '__main__':
    centers, radii, sum_radii = pack_circles()

    if sum_radii < 2.65:
        print('Should be better!')
        assert False
    
    if not is_valid(centers, radii):
        print('Invalid packing!')
        assert False