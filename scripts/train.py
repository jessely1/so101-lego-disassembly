"""
Training script for SO101 Lego Disassembly - Imitation Learning
Uses LeRobot ACT policy with demonstration dataset from Hugging Face
"""

import subprocess


def train(
    dataset_repo_id="Jessely/lego_disassembly2",
    policy_repo_id="Jessely/lego_disassembly2_act",
    output_dir="outputs/train/lego_disassembly",
    steps=100000,
    resume=False,
):
    """Train ACT policy on lego disassembly dataset."""
    cmd = [
        "lerobot-train",
        f"--dataset.repo_id={dataset_repo_id}",
        "--policy.type=act",
        f"--policy.repo_id={policy_repo_id}",
        f"--output_dir={output_dir}",
        f"--steps={steps}",
    ]

    if resume:
        cmd.append("--resume=true")

    print("Starting training...")
    print(f"Dataset: {dataset_repo_id}")
    print(f"Steps: {steps}")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    train()
