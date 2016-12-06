This module provides code used to compute and verify the results in the paper, "Applications of Conformal Geometric Algebra to Transmission Line Theory", by Alex Arsenovic. There are 3 files interest. 

* `SymbolicComputation` presents some of the derivations for the paper. It uses the  symbolic geometric algebra module  `galgebra`

* `NumericalVerification` is used as a test-suite to  verify  the results agree with conventional functions in complex algebra. This module uses the python module `clifford`. 

* `cgatline.py` numerical implementation of the results, given in a python module.
