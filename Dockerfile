# Use a recent slim Python image
FROM python:3.12-slim
LABEL maintainer="Scott Gibb"

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Clean up apt cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Add uv to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv pip install --system --no-cache .

# Default command
ENTRYPOINT ["python3"]
CMD ["-u", "src/Main.py"]