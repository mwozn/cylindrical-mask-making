# cylindrical-mask-making

[![DOI](https://zenodo.org/badge/755336442.svg)](https://zenodo.org/doi/10.5281/zenodo.10988629)

1. Use IMOD's 3dmod to click two points within a volume & save model to .mod file.
2. Use IMOD's model2point to convert .mod to .pt file.
3. Use points_for_cylinder_mask.py to generate the points for mask making.
4. Convert points file back to mod file with IMOD's point2model
5. Use make_mask_from_model.py to generate the mask from points for cylinder.

