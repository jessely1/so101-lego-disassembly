# SO101 Lego Disassembly — Imitation Learning

Final project for the Intelligent Control Module at ITESM.

## Task
The SO101 robot arm learns to pick lego pieces by color (red, white, grey) and place them in a target base using Imitation Learning (ACT policy).

## Technical Track
Track 1: Imitation Learning / Behaviour Cloning using ACT (Action Chunking Transformer)

## Dataset
- 150 demonstrations (50 per class)
- Classes: red lego, white lego, grey lego
- Hosted on Hugging Face: https://huggingface.co/datasets/Jessely/lego_disassembly1

## Trained Model
- Policy: ACT (Action Chunking Transformer)
- Training steps: 100,000
- Final loss: 0.044
- Model hosted on Hugging Face: https://huggingface.co/Jessely/lego_disassembly1_act

## Installation
pip install lerobot[feetech]
pip install lerobot[dataset]
pip install lerobot[training]

## Dataset Link
https://huggingface.co/datasets/Jessely/lego_disassembly1

## Model Link
https://huggingface.co/Jessely/lego_disassembly1_act

## Team
ITESM — Intelligent Control Module
