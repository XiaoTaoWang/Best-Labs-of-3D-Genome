Description
===========
This repository contains data I collected and the co-authored networks I extracted
from publication records when I selected appropriate labs for my postdoctoral training
recently.

Actually, I used a simple data mining algorithm on publication data. I transformed the
problem of searching good labs into searching good corresponding authors, although they
are not exactly the same thing. I expected to use the number of works, total times cited
by others, and collaboration networks to evaluate the impact of a researcher on a specific
field (here is the 3D genome). Fortunately, the publication records downloaded from web
of science contain all these information. So the most important part of my work was to
collect enough relevant records. From the original searched results in web of science,
I checked the title and the abstract one by one, and removed those not relevant to 3D genome.
Finally, I collected near 2000 publication records. And from this pool, I extracted a
weighted network with nodes as corresponding authors and edge weights as the number of times
those authors co-wrote a paper.

From this network, I selected the most influential 68 researchers and by investigating their
lab website, I chose the most relevant 16 labs ...

Here's the co-authored network of these 68 researchers:

.. image:: ./networks/best-PI-network.pdf
        :align: center
