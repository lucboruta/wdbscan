wdbscan
=======

Python implementation of a weighted extension of [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) (Ester et al., 1996).

This module provides a weighted implementation of Ester et al.'s algorithm, accomodating instance weights. Here, a core object is not defined as an object whose epsilon-neighborhood contains at least a given number of objects, but as an object whose epsilon-neighborhood weighs a least a given weight. The weight of a given object's epsilon-neighborhood is straightforwardly defined as the sum of the weights of its epsilon-neighbors. This implementation does not require weights to be positive, so be careful what you wish for, you might just get it.

To use this module, you must have [NumPy](http://numpy.scipy.org/) installed.

## License

*[Do What The Fuck You Want To Public License](http://en.wikipedia.org/wiki/WTFPL)* (version 2).

## Citation

When using *wdbscan* for a publication, please cite my [doctoral dissertation](http://tel.archives-ouvertes.fr/tel-00746163).

    @phdthesis{
        author = {Boruta, Luc},
        title = {Indicators of Allophony and Phonemehood},
        school = {Universit{\'e} Paris Diderot},
        year = {2012},
    }