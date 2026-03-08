from arl import WarmPoolManager

POOL_NAME = "csc4001-pool"
NAMESPACE = "default"
GATEWAY_URL = "http://10.10.10.220:30076"  # 或你实际的 Gateway 地址


def main() -> None:
    mgr = WarmPoolManager(
        namespace=NAMESPACE,
        gateway_url=GATEWAY_URL,
        timeout=600,  # 最大等待时间，秒
    )

    # 把 WarmPool 的 replicas 调整到 8
    mgr.scale_warmpool(POOL_NAME, replicas=200)

    # 等待该 WarmPool 至少有 8 个 ready 副本
    mgr.wait_for_ready(
        POOL_NAME,
        timeout=600,
        poll_interval=2.0,
        min_ready=8,
    )

    print(f"WarmPool {POOL_NAME} 已扩容到 8 个 ready 副本")


if __name__ == "__main__":
    main()
