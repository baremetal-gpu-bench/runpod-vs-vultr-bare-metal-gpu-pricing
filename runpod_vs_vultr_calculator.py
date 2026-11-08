#!/usr/bin/env python3
"""RunPod vs Vultr Cloud GPU TCO Calculator 2026."""
import argparse

def calculate(hours_per_month=150):
    # RunPod Community/Secure Cloud: A100 80GB on-demand ~$1.89/hr.
    runpod_hourly = 1.89
    runpod_total = hours_per_month * runpod_hourly

    # Vultr Cloud GPU: A100 80GB dedicated enterprise ~$2.60/hr.
    vultr_hourly = 2.60
    vultr_total = hours_per_month * vultr_hourly

    diff = vultr_total - runpod_total

    print("=" * 65)
    print("RunPod vs Vultr: 150 Hours A100 80GB Benchmark")
    print("=" * 65)
    print(f"RunPod Cloud (@$1.89/hr):   ${runpod_total:.2f}/mo")
    print(f"Vultr Cloud GPU (@$2.60/hr):${vultr_total:.2f}/mo")
    print(f"Monthly Cost Difference:    ${diff:.2f}/mo ({'RunPod Cheaper' if diff > 0 else 'Vultr Cheaper'})")
    print(f"Enterprise SLA Note:        Vultr includes 100% SLA and full bare-metal isolation")
    print("=" * 65)
    return runpod_total, vultr_total

if __name__ == "__main__":
    calculate()
