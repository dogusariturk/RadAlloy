<div align="center">

# RadAlloy

**Radiation Damage Simulation for Alloys**

[![Python](https://img.shields.io/badge/python-3.11+-brightgreen.svg)](https://www.python.org/)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Nimplex Tests](https://github.com/dogusariturk/RadAlloy/actions/workflows/test_nimplex.yml/badge.svg)](https://github.com/dogusariturk/RadAlloy/actions/workflows/test_nimplex.yml)

RadAlloy is a Python package designed for simulating radiation damage in metallic alloys. This tool provides computational methods to analyze and predict the behavior of materials under radiation exposure, which is crucial for nuclear applications and materials science research.

<p>
  <a href="https://github.com/dogusariturk/RadAlloy/issues/new?labels=bug">Report a Bug</a> |
  <a href="https://github.com/dogusariturk/RadAlloy/issues/new?labels=enhancement">Request a Feature</a>
</p>

</div>

---

## Features

- **Nuclear Activation Prediction**: Comprehensive nuclear activation analysis for alloy compositions
- **Component Space Generation**: Efficient generation of compositional spaces using N-dimensional simplex sampling
- **Interactive Visualization**: Built-in 2D and 3D plotting of composition space for 3- and 4- component systems

## Installation

### Requirements

- **Python**: 3.11 or higher
- **Nim**
  - For installation instructions, see the [nim installation guide](https://nim-lang.org/install.html).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/dogusariturk/RadAlloy.git
   cd RadAlloy
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

---

## License

This project is under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
