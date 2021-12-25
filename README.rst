Description
===========
This repository contains collaboration networks I built to evaluate the impact
and contributions of labs in 3D genome research. The code however can be easily
modified to rank labs in any other scientific field.

The pipeline is quite simple:

  1. Search and download 3D genome related publication records through `web of science <https://clarivate.com/webofsciencegroup/solutions/web-of-science/>`_
  2. Parse and extract necessary information (authors, citation times, ... ) from the records
  3. Count the number of publications and total cited times of each corresponding author
  4. Build the co-author network
  5. Rank labs by their centrality in the network, total cited times, and number of publications.

Collaboration Networks
======================
I plan to update the network annually and each update will include data from last 5 years.

- `Year 2008 - 2017 <networks/2008-2017/report.rst>`_
- `Year 2015 - 2019 <networks/2015-2019/report.rst>`_
- `Year 2017 - 2021 <networks/2017-2021/report.rst>`_
