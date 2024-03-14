## Deep-Learning-for-Quantum Mechanics(QM)--Quantum parameter estimation

This repository contains the project for quantum parameter estimation.
In this project, our aim was to characterize an open quantum system based on a single measurement. In this case, we assume to have a 2-level system that is being Rabi driven with a Rabi frequency $\Omega$ and has a typical decay rate $\gamma$. 
The graph we obtain after one repetition is as follows:
![image](https://github.com/ariels1234/Deep-Learning-for-QM/assets/71715388/377a8807-0fe6-4bdd-a14f-a8dabd17a85c)

In this graph, one can see the excited state population vs. time. In blue, one can observe a single measurement where we have a drive combined with quantum jumps dictated by the decay rate $\gamma$. Only, after averaging these measurements many times, one can reach the orange curve, which is given by the Lindblad master equation as:

$\dot{\rho}(t)=-\frac{i}{\hbar}\left[H(t),\rho(t)\right]+\sum_{n}\frac{1}{2}\left[2C_{n}\rho(t)C_{n}^{\dagger}-\rho(t)C_{n}^{\dagger}C_{n}-C_{n}^{\dagger}C_{n}\rho(t)\right]$

where one can induce the system parameters by solving this equation and fitting it to the averaged measurement results (>>1). 

Our NN managed to find the two parameters of the system $\gamma$ and $\Omega$ (assuming there is no detuning) very effectively -> 100% accuracy! 
We utilized a convolutional neural network (CNN) for this task. 


One can find:

- A PDF presentation of the project that Yakov Solomons and myself, Ariel Smooha, performed and presented in the ML course of Prof. Eilam Gross 2021.

- The dataloader.py code for loading the training and validation sets
- The model.py code where the neural network (NN) is set
- The Project_CNN.ipynb file where the training and the validation of the NN are perfromed using the above .py files.
- The trained_model.pt files, which is the trained NN ready for use after performing the training
- The data set which was generated using a Monte Carlo simulation (master.py code)
