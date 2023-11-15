# To build this container, go to ILAMB-Workflow root folder and execute:
# docker build -t accessnri/ilamb:latest . -f docker/Dockerfile
FROM condaforge/mambaforge

WORKDIR /src/ILAMB
COPY environment.yml .
RUN mamba update -y conda mamba pip && mamba env create --name ilamb --file environment.yml && conda clean --all -y

# Make RUN commands use the new environment:
SHELL ["conda", "run", "--name", "ilamb", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--name", "ilamb", "ilamb-run"]
