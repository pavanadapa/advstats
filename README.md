<div align="center">
  <img src="https://pavanadapa.github.io/Images/AdvStatslogo.png"><br>
</div>

# Library for mathematical analysis of various sampling methods

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/pavanadapa/advstats/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About

AdvStats is a python library for mathematical analysis of various sampling methods. So far the package supports analysis on cluster samples and stratifed samples. And the functions support various data formats. If using data from a table, the data can stored in two ways.

### 1

| Data          | Cluster/ Stratum   |
| ------------- | ------------------ |
| Data Point 1  | Cluster/ Stratum 1 |
| Data Point 2  | Cluster/ Stratum 2 |

### 2

| Cluster/ Stratum 1 | Cluster/ Stratum 2 |
| ------------------ | ------------------ |
| Data Point 1       | Data Point 3       |
| Data Point 2       | Data Point 4       |

The required supporting can also just be manually entered. For more information look at the documentation or the tests. 

## Installion

```sh
pip install advstats
```

## Documentation

Documetation for the package can be found at pavanadapa.github.io(pavanadapa.github.io).

## Future
Implementation of a two-stage cluster sampling and more sampling methods are coming soon. 