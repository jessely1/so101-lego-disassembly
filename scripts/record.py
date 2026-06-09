"""
Recording script for SO101 Lego Disassembly demonstrations

Usage:
    python scripts/record.py

Or run directly:
    lerobot-record \
        --robot.type=so101_follower \
        --robot.port=COM4 \
        --robot.id=my_follower \
        --teleop.type=so101_leader \
        --teleop.port=COM3 \
        --teleop.id=my_leader \
        --robot.cameras="{ phone: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}" \
        --dataset.repo_id=Jessely/lego_disassembly2 \
        --dataset.num_episodes=50 \
        --dataset.single_task="Pick red lego and place in green base" \
        --dataset.episode_time_s=30 \
        --dataset.reset_time_s=10 \
        --display_data=true \
        --resume=true
"""

import subprocess


def record(
    robot_port="COM4",
    leader_port="COM3",
    dataset_repo_id="Jessely/lego_disassembly2",
    num_episodes=50,
    task="Pick red lego and place in green base",
):
    """Record demonstrations for lego disassembly task."""
    cmd = [
        "lerobot-record",
        "--robot.type=so101_follower",
        f"--robot.port={robot_port}",
        "--robot.id=my_follower",
        "--teleop.type=so101_leader",
        f"--teleop.port={leader_port}",
        "--teleop.id=my_leader",
        '--robot.cameras={ phone: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30}}',
        f"--dataset.repo_id={dataset_repo_id}",
        f"--dataset.num_episodes={num_episodes}",
        f"--dataset.single_task={task}",
        "--dataset.episode_time_s=30",
        "--dataset.reset_time_s=10",
        "--display_data=true",
        "--resume=true",
    ]
    print(f"Recording {num_episodes} episodes...")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    record()
