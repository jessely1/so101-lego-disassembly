# SO101 Lego Disassembly — Imitation Learning

Final project for the Intelligent Control Module at ITESM.

## Selected Task
Option 1: Lego Storage — The SO101 robot arm learns to pick lego pieces by color (red, white, grey) and place them in a target base using Imitation Learning.

## Technical Track
Track 1: Imitation Learning / Behaviour Cloning using ACT (Action Chunking Transformer)

## Dataset
- 430+ demonstrations across 3 classes
- Classes: red lego, white lego, grey lego
- Hosted on Hugging Face: https://huggingface.co/datasets/Jessely/lego_disassembly2

## Trained Model
- Policy: ACT (Action Chunking Transformer)
- Training steps: 100,000
- Final loss: ~0.057
- Model: https://huggingface.co/Jessely/lego_disassembly2_act

## Installation

    pip install -r requirements.txt

## Docker

    docker build -t so101-lego-disassembly .
    docker run --rm -it so101-lego-disassembly

## Recording Demonstrations

    python scripts/record.py

## Training

    python scripts/train.py

## Evaluation

    python scripts/evaluate.py

## Results
- Training loss: 0.057 (100K steps)
- Robot successfully moves toward target position
- Limitation: inference speed 11Hz vs 30Hz target

## Repository Structure

    so101-lego-disassembly/
    README.md
    Dockerfile
    requirements.txt
    data/
        dataset_link.md
    scripts/
        train.py
        evaluate.py
        record.py
    results/
        metrics/
        plots/
        videos/

## Team
ITESM — Intelligent Control Module
