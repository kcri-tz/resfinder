# Slimmed down ResFinder repository

This repository is a slimmed down copy of the upstream repository at
<https://bitbucket.org/genomicepidemiology/resfinder>.  It exists to
enable rapid download of this CGE service.

The code in this repository is periodically updated from the upstream repo,
and version tags mirror the upstream tags, with a fourth decimal added to
indicate the exact commit that was copied over.  For instance:

    $ git describe (upstream)  →  $ git describe (here)
    3.0.2-6-g6dfe              →  3.0.2.6  (6th commit after 3.0.2)

Note that test data and other extraneous upstream files are omitted
from this repository.

The reason for maintaining this repository (and the other slimmed down
repos at <https://github.com/kcri-tz/>) was that several CGE services,
due to spurious binary commits in the past, have massive git histories.

Upstream now provides binary downloads and a simple `pip` install, which
is now the recommended mode of installation.  This repository is still
used for the [CGE Bacterial Analysis Pipeline](https://github.com/zwets/cge-bap)
but will be discarded in the near future.

