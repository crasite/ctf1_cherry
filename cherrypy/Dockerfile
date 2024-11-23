FROM cgr.dev/chainguard/python@sha256:76b93ba9466714276b0407aef4b464e3a9dfd3190f1d68ac0bed9e1bbe9b172d AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --user --no-cache-dir

FROM cgr.dev/chainguard/python@sha256:5e7e242e9f587737df9864210c90810bbfb07a68d55ef8a2d314b8a3212fc10e

WORKDIR /app

# Make sure you update Python version in path
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages

COPY main.py .

ENTRYPOINT [ "python", "main.py"  ]
