# Py_FS: A Python Package for Feature Selection
Py_FS is a toolbox developed with complete focus on Feature Selection (FS) using Python as the underlying programming language. It comes with capabilities like nature-inspired evolutionary feature selection algorithms, filter methods and simple evaulation metrics to help with easy applications and comparisons among different feature selection algorithms over different datasets. It is still in the development phase. We wish to extend this package further to contain more extensive set of feature selection procedures and corresponding utilities.

<p align="center">  
  <img src="https://github.com/Ritam-Guha/Py_FS/blob/master/Images/logo.jpg" height="300" width="300">
</p><br>

## Installation

Please install the required utilities for the package by running this piece of code:

    pip3 install -r requirements.txt

The package is publicly avaliable at **PYPI: Python Package Index**.
Anybody willing to use the package can install it by simply running:
    
    pip3 install Py_FS



## Structure

The current structure of the package is mentioned below. Depending on the level of the function intended to call, it should be imported using the period(.) hierarchy.

### Py_FS

* [filter/](./Py_FS/filter)
  * [MI.py](./Py_FS/filter/MI.py)
  * [PCC.py](./Py_FS/filter/PCC.py)
  * [Relief.py](./Py_FS/filter/Relief.py)
  * [SCC.py](./Py_FS/filter/SCC.py)
* [wrapper/](./Py_FS/wrapper)
  * [nature_inspired/](./Py_FS/wrapper/nature_inspired)
    * [BBA.py](./Py_FS/wrapper/nature_inspired/BBA.py)
    * [CS.py](./Py_FS/wrapper/nature_inspired/CS.py)
    * [EO.py](./Py_FS/wrapper/nature_inspired/EO.py)
    * [GA.py](./Py_FS/wrapper/nature_inspired/GA.py)
    * [GSA.py](./Py_FS/wrapper/nature_inspired/GSA.py)
    * [GWO.py](./Py_FS/wrapper/nature_inspired/GWO.py)
    * [HS.py](./Py_FS/wrapper/nature_inspired/HS.py)
    * [MF.py](./Py_FS/wrapper/nature_inspired/MF.py)
    * [PSO.py](./Py_FS/wrapper/nature_inspired/PSO.py)
    * [RDA.py](./Py_FS/wrapper/nature_inspired/RDA.py)
    * [SCA.py](./Py_FS/wrapper/nature_inspired/SCA.py)
    * [WOA.py](./Py_FS/wrapper/nature_inspired/WOA.py)
* [evaluation.py](./Py_FS/evaluation.py)


For example, if someone wants to use GA, it should be imported using the following statement:

    import Py_FS.wrapper.nature_inspired.GA

There are mainly three utilities in the current version of the package. The next part discusses these
three parts in detail:

## 1. Wrapper-based Nature-inpsired Feature Selection
Wrapper-based Nature-inspired methods are very popular feature selection approaches due to their efficiency and simplicity. These methods progress by introducing random set of candidate solutions (agents which are natural elements like particles, whales, bats etc.) and improving these solutions gradually by using guidance mechanisms from fitter agents. In order to calculate the fitness of the candidate solutions, wrappers require some learning algorithm (like classifiers) to calculate the goodness of a solution at every iteration. This makes wrapper methods extremely reliable but computationally expensive as well.

Py_FS currently supports the following 12 wrapper-based FS methods:
* Binary Bat Algorithm (BBA)
* Cuckoo Search Algorithm (CS)
* Equilibrium Optimizer (EO)
* Genetic Algorithm (GA)
* Gravitational Search Algorithm (GSA)
* Grey Wolf Optimizer (GWO)
* Harmony Search (HS)
* Mayfly Algorithm (MA)
* Particle Swarm Optimization (PSO)
* Red Deer Algorithm (RDA)
* Sine Cosine Algorithm (SCA)
* Whale Optimization Algorithm (WOA)

These wrapper approached can be imported in your code using the following statements:
    
    import Py_FS.wrapper.nature_inspired.BBA
    import Py_FS.wrapper.nature_inspired.CS
    import Py_FS.wrapper.nature_inspired.EO
    import Py_FS.wrapper.nature_inspired.GA
    import Py_FS.wrapper.nature_inspired.GSA
    import Py_FS.wrapper.nature_inspired.GWO
    import Py_FS.wrapper.nature_inspired.HS
    import Py_FS.wrapper.nature_inspired.MA
    import Py_FS.wrapper.nature_inspired.PSO
    import Py_FS.wrapper.nature_inspired.RDA
    import Py_FS.wrapper.nature_inspired.SCA
    import Py_FS.wrapper.nature_inspired.WOA

## 2. Filter-based Feature Selection
Filter methods do not use any intermediate learning algorithm to verify the strength of the generated solutions. Instead, they use statistical measures to identify the importance of different features in the context. So, finally every feature gets a rank according to their relevance in the dataset. The top features can then be used for classification. 

Py_FS currently supports the following 4 filter-based FS methods:
* Pearson Correlation Coefficient (PCC)
* Spearman Correlation Coefficient (SCC)
* Relief
* Mutual Information (MI)

These filter approached can be imported in your code using the following statements:
    
    import Py_FS.filter.PCC
    import Py_FS.filter.SCC
    import Py_FS.filter.Relief
    import Py_FS.filter.MI

## 3. Evaluation Metrics
The package comes with tools to evaluate features before or after FS. This helps to easily compare and analyze 
performances of different FS procedures. 

Py_FS currently supports the following evaluation metrics:
* classification accuracy
* average recall
* average precision
* average f1 score
* confusion matrix
* confusion graph

The evaulation capabilities can be imported in your code using the following statement:
    
    from Py_FS.evaulation import evaluate
