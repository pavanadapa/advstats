<div align="center">
  <img src="Images\AdvStats.png"><br>
</div>

<h2 align="center">Library for mathematical analysis of various sampling methods</h2>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

##About

AdvStats is a python library for mathematical analysis of various sampling methods. So far the package supports analysis on cluster samples and stratifed samples. And the functions support various data formats. If using data from a table, the data can stored in two ways.

###1

| Data          | Cluster/ Stratum   |
| ------------- | ------------------ |
| Data Point 1  | Cluster/ Stratum 1 |
| Data Point 2  | Cluster/ Stratum 2 |

###2

| Cluster/ Stratum 1 | Cluster/ Stratum 2 |
| ------------------ | ------------------ |
| Data Point 1       | Data Point 3       |
| Data Point 2       | Data Point 4       |

The required supporting can also just be manually entered. For more information look at the documentation. 

##Installion

```sh
pip install advstats
```

##Documentation

Documetation for the package can be found at pavanadapa.github.io(pavanadapa.github.io).

##Future
Implementation of a two-stage cluster sampling and more sampling methods are coming soon. 