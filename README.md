# SO101 Lego Disassembly — Imitation Learning

Final project for the Intelligent Control Module at ITESM.

## Members

- Gustavo Alexander Nuño Corvera - 100%
- Luis Carlos Ortiz de Montellano Gómez - 100%
- Jessely Santiago Bahena - 100%
- Alfredo Garzon Murillo - 50%

## Selected Task

Option 1: Lego Storage — The SO101 robot arm learns to pick Lego pieces by color (red, white, grey) and place them in a target base using Imitation Learning.

## Technical Track

Track 1: Imitation Learning / Behaviour Cloning using ACT (Action Chunking Transformer)

## Hardware Requirements

To use this project, you will need:

* **Two assembled SO101 robot arms**

  * One configured as the **Leader** arm
  * One configured as the **Follower** arm
* **A USB camera** for recording demonstrations and datasets
* **At least three available USB ports on your computer**

  * One for the Leader arm
  * One for the Follower arm
  * One for the camera

> **Note:** The camera is **not required for teleoperation**, but it **is required for recording datasets** that will later be uploaded to Hugging Face and used for training.

## Software Requirements

This project depends on the **LeRobot** framework from Hugging Face. Before using the scripts in this repository, clone and set up the LeRobot repository:

https://github.com/huggingface/lerobot

Follow the installation instructions provided by LeRobot to configure the environment and robot interfaces.

## Dataset

* 430+ demonstrations across 3 classes
* Classes: red Lego, white Lego, grey Lego
* Hosted on Hugging Face: https://huggingface.co/datasets/Jessely/lego_disassembly2

## Trained Model

* Policy: ACT (Action Chunking Transformer)
* Training steps: 100,000
* Final loss: 0.057
* Model: https://huggingface.co/Jessely/lego_disassembly2_act

## Checkpoints

Model checkpoints are available on Hugging Face (too large for GitHub):

* Final model: https://huggingface.co/Jessely/lego_disassembly2_act
* Red Lego model: https://huggingface.co/Jessely/lego_red_act (in progress)
* White Lego model: https://huggingface.co/Jessely/lego_white_act (in progress)
* Grey Lego model: https://huggingface.co/Jessely/lego_grey_act (in progress)

## Installation

```bash
pip install -r requirements.txt
```

## Docker

```bash
docker build -t so101-lego-disassembly .
docker run --rm -it so101-lego-disassembly
```

## Recording Demonstrations

```bash
python scripts/record.py
```

Requires:

* Leader SO101 connected
* Follower SO101 connected
* USB camera connected

## Training

```bash
python scripts/train.py
```

## Evaluation

```bash
python scripts/evaluate.py
```

## Results

* Training loss: 0.057 (100K steps)
* Robot successfully follows trajectories similar to demonstrations
* Robot places Lego in the correct base when the grasp succeeds
* Limitation: inference speed of 11 Hz versus the 30 Hz target causes precision issues

## Repository Structure

```text
so101-lego-disassembly/
├── README.md
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   └── record.py
└── results/
    ├── metrics/
    ├── plots/
    └── videos/
```

## Team

ITESM — Intelligent Control Module
