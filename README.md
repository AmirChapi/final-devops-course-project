feature/readme-conflict
# QuakeWatch (Phase 1) - Conflict Demo


# QuakeWatch (Phase 1) - Helm Docs
 main
Simple Python Flask app returning "Hello, World!".

## Run locally (no Docker)
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000

 feature/readme-conflict
## Helm Deployment

This section demonstrates a conflicting change.

helm pull oci://ghcr.io/amirchapi/helm-charts/final-app --version 0.1.1
## Helm Chart

The application is packaged as a Helm chart and published to an OCI-based
artifact repository (GitHub Container Registry).

**Chart location:**
- `helm/final-app`

**Published artifact:**
- `ghcr.io/amirchapi/helm-charts/final-app:0.1.0`

**Pull the chart:**
```bash
helm pull oci://ghcr.io/amirchapi/helm-charts/final-app --version 0.1.0
main
