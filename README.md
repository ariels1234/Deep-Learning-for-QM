## Deep-Learning-for-QM

This repository contains the project for quantum parameter estimation.
In this project, our aim was to characterize an open quantum system based on a single measurement. In this case we assume to have a 2 level system which is rabi driven has a typical decay rate $\gamma$ 



One can find:

- A PDF presentation of the project that Yakov Solomons and myself, Ariel Smooha, performed and presented in the ML course of Prof. Eilam Gross 2021.

- The dataloader.py code for loading the training and validation sets
- The model.py code where the neural network (NN) is set
- The Project_CNN.ipynb file where the training and the validation of the NN are perfromed using the above .py files.
- The trained_model.pt files, which is the trained NN ready for use after performing the training
- The data set which was generated using a Monte Carlo simulation (master.py code)
