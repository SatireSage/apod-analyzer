# 📡 NASA Astronomy Picture of the Day (APOD) Analyzer

[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=SatireSage/apod-analyzer&file=colour_palette.m)

This project automates the retrieval and analysis of NASA's [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/) using a self-hosted runner (Linux Machine/Raspberry Pi), GitHub Actions, and MATLAB. 
It showcases how [MATLAB GitHub Actions](https://github.com/matlab-actions) can be used in continuous workflows.

## Today's Picture:
<div align="center">
  <a href="https://apod.nasa.gov/apod/" target="_blank">
    <img src="./apod/apod.jpg?" alt="Astronomy Picture of the Day" width="600" />
  </a>
  <br>
  <em style="font-size: 18px; color: #555;">Astronomy Picture of the Day (APOD)</em>
</div>

## Breakdown:

1. **GHA Cron Trigger:** A GitHub Actions scheduler runs periodically to start the workflow.
2. **API Call (Python):** A Python script fetches the latest APOD from the [NASA API](https://api.nasa.gov/).
3. **MATLAB Analysis:** MATLAB processes and analyzes the image using image processing tools.
4. **Results:** The pipeline generates visual or numeric results such as color palettes, histograms, etc.

<div align="center">
  <br/>
  <img src="https://github.com/user-attachments/assets/36bfa1ec-cee0-469c-aa73-84c8f32d96b9" alt="Workflow Diagram" width="500"/>
  <br/>
  <em style="font-size: 18px; color: #555;">Workflow</em>
</div>
<br/>

The goal is to showcase [MATLAB Actions](https://github.com/matlab-actions) to run such a flow in MATLAB on a self-hosted runner and perform further analysis of the image(s)
using toolboxes such as the [Image Processing Toolbox](https://www.mathworks.com/products/image-processing.html)

## Authors

- [Sahaj Singh](https://www.github.com/satiresage)
- [Yann Debray](https://www.github.com/yanndebray)
- [Yann Debray](https://www.github.com/tharikaa-kumar)
