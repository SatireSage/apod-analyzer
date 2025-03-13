# NASA Astronomy Picture of the Day (APOD) Analyzer: [![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=SatireSage/apod-analyzer&file=colour_palette.m)

This flow automatically fetches NASA's Astronomy Picture of the Day (APOD) using a Raspberry Pi and GitHub Actions, then analyzes the image using MATLAB (or MATLAB Online).

## Workflow:

1. **Fetch Image:** A Raspberry Pi regularly retrieves the latest APOD from [NASA API](https://api.nasa.gov/)
2. **Continuous Integration:** GitHub Actions triggers the MATLAB analysis script whenever a new APOD is fetched and uploaded.
3. **MATLAB Analysis:** The APOD image is analyzed with MATLAB, generating insights and visualizations.

This integration showcases a seamless workflow between hardware, cloud automation, and analytical software.

## Today's Picture:
<p align="center">
  <a href="https://apod.nasa.gov/apod/">
    <img src="./apod/apod.jpg" alt="APOD" width="600" style="border-radius: 8px;">
  </a>
  <br>
  <em>Astronomy Picture of the Day (APOD)</em>
</p>

## Authors

- [Sahaj Singh](https://www.github.com/satiresage)
- [Yann Debray](https://www.github.com/slevin48)
