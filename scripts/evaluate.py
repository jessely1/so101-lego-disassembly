"""
Evaluation script for SO101 Lego Disassembly - Imitation Learning
Runs the trained ACT policy on the physical robot

Usage:
    python scripts/evaluate.py

Or run directly:
    lerobot-rollout \
        --robot.type=so101_follower \
        --robot.port=COM4 \
        --robot.id=my_follower \
        --robot.cameras="{ phone: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" \
        --policy.type=act \
        --policy.pretrained_path=outputs/train/lego_disassembly/checkpoints/last/pretrained_model \
        --policy.input_features="{ observation.images.phone: {type: VISUAL, shape: [3, 480, 640]}, observation.state: {type: STATE, shape: [6]}}" \
        --policy.output_features="{ action: {type: ACTION, shape: [6]}}" \
        --policy.device=cuda \
        --task="Pick red lego and place in green base"
"""

import subprocess


def evaluate(
    robot_port="COM4",
    task="Pick red lego and place in green base",
    pretrained_path="outputs/train/lego_disassembly/checkpoints/last/pretrained_model",
):
    """Run rollout on physical robot."""
    cmd = [
        "lerobot-rollout",
        "--robot.type=so101_follower",
        f"--robot.port={robot_port}",
        "--robot.id=my_follower",
        "--robot.cameras={ phone: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}",
        "--policy.type=act",
        f"--policy.pretrained_path={pretrained_path}",
        "--policy.input_features={ observation.images.phone: {type: VISUAL, shape: [3, 480, 640]}, observation.state: {type: STATE, shape: [6]}}",
        "--policy.output_features={ action: {type: ACTION, shape: [6]}}",
        "--policy.device=cuda",
        f"--task={task}",
    ]
    print(f"Running rollout on robot at {robot_port}...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    evaluate()
