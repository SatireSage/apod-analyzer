# NASA Astronomy Picture of the Day (APOD) Analyzer: [![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=SatireSage/apod-analyzer&file=colour_palette.m)

This flow automatically fetches NASA's Astronomy Picture of the Day (APOD) using a Raspberry Pi and GitHub Actions, then analyzes the image using MATLAB (or MATLAB Online).

## Workflow:

1. **Fetch Image:** A Raspberry Pi regularly retrieves the latest APOD from [NASA API](https://api.nasa.gov/)
2. **Continuous Integration:** GitHub Actions triggers the MATLAB analysis script whenever a new APOD is fetched and uploaded.
3. **MATLAB Analysis:** The APOD image is analyzed with MATLAB, generating insights and visualizations.

The goal is to showcase [MATLAB Actions](https://github.com/matlab-actions) to run such a flow in MATLAB on a self-hosted runner and perform further analysis of the image(s)
using toolboxes such as the [Image Processing Toolbox](https://www.mathworks.com/products/image-processing.html)

## Today's Picture:
<div align="center">
  <a href="https://apod.nasa.gov/apod/" target="_blank">
    <img src="./apod/apod.jpg" alt="Astronomy Picture of the Day" width="600" />
  </a>
  <br>
  <em style="font-size: 18px; color: #555;">Astronomy Picture of the Day (APOD)</em>
</div>

## Authors

- [Sahaj Singh](https://www.github.com/satiresage)
- [Yann Debray](https://www.github.com/yanndebray)
