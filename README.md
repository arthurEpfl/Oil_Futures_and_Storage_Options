# Financial Derivatives Calibration and Monte Carlo Simulation

This code focuses on the calibration of parameters and Monte Carlo simulations for pricing and analyzing storage options.

## Project Structure

- `monte-carlo.ipynb`: Jupyter notebook for running Monte Carlo simulations to price the storage options.
- `calibration.ipynb`: Jupyter notebook for calibrating the parameters of the financial derivatives model.
- `functions.py`: Python script containing utility functions used across the notebooks.
- `requirements.txt`: File containing the required Python libraries and their versions.
- `Project-Data.csv`: CSV file containing the futures prices used for calibration.

## Installation

**Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Notebooks

### Calibration Notebook

- **File**: `calibration.ipynb`
- **Description**: This notebook performs the calibration of several parameters of the financial derivatives model, including:
  - Mean reversion intensity \( \lambda_r \)
  - Long-term mean \( \bar{\lambda} \)
  - Initial value \( r_0 \) of the risk-free rate
  - Mean reversion intensity \( \lambda_\delta \)
  - Long-term mean \( \bar{r} \)
  - Initial value \( \delta_0 \)

### Monte Carlo Simulation Notebook

- **File**: `monte-carlo.ipynb`
- **Description**: This notebook runs Monte Carlo simulations to calculate the payoff of the storage option at the start date, the critical value of the convenience yield, and the initial price of the storage option as functions of the start date \( T_0 \), the storage period \( \Delta \), and the storage cost \( \alpha \). It also visualizes these metrics against various parameters using plots.

## Utility Functions

- **File**: `functions.py`
- **Description**: This script contains utility functions such as the calculation of \(\psi_0\) and \(\psi_\delta\)

## Usage

1. **Run the Calibration Notebook**:
    - Open `calibration.ipynb`.
    - Execute the cells to perform the calibration of the financial model parameters.

2. **Run the Monte Carlo Simulation Notebook**:
    - Open `monte-carlo.ipynb` in Jupyter Notebook or Jupyter Lab.
    - Execute the cells to perform the Monte Carlo simulations and visualize the results.

## Data

- **Project-Data.csv**: Contains the futures prices and yields used for calibration. Ensure this file is in the same directory as the notebooks when running them.

## Dependencies

The project requires the following Python libraries, which are listed in `requirements.txt`:

- `matplotlib==3.5.1`
- `numpy==1.24.3`
- `pandas==1.3.4`
- `scipy==1.5.4`


