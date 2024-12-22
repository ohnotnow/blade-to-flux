import os
import time
import argparse
import subprocess
from pydantic_ai import Agent
from yaspin import yaspin
from costing import get_cost

def ensure_in_flux_branch():
    if "flux" not in subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip():
        raise Exception("You must be in a flux branch to run this script")

def get_agent(model_name: str = "gpt-4o-mini", system_prompt: str = ""):
    if not system_prompt:
        system_prompt = get_system_prompt()
    return Agent(model_name=model_name, system_prompt=system_prompt)

def get_system_prompt():
    with open("system_prompt.txt", "r") as file:
        return file.read()

def find_all_blade_files(directory: str):
    return [f for f in os.listdir(directory) if f.endswith(".blade.php")]

def process_blade_file(file_path: str, model_name: str):
    agent = get_agent(model_name=model_name)
    with yaspin(text=f"Processing: {file_path}", spinner=True, color="cyan") as spinner:
        with open(file_path, "r") as file:
            template_content = file.read()
        response = agent.run_sync(template_content)
        updated_content = strip_markdown(response.data)
    return updated_content, response.cost()

def process_all_blade_files(directory: str, model_name: str, start_file: str = ""):
    total_cost = 0
    start_time = time.time()
    should_start = start_file == ""
    for file_path in find_all_blade_files(directory):
        print(f"File: {file_path}")
        exit()
        if not should_start:
            if file_path == start_file:
                should_start = True
            else:
                continue
        updated_content, cost = process_blade_file(file_path, model_name)
        with open(file_path, "w") as file:
            file.write(updated_content)
        total_cost += get_cost(model_name, cost)
    end_time = time.time()
    total_time = end_time - start_time
    return total_cost, total_time

def strip_markdown(content: str):
    tags = ["blade", "markdown", "php", "html", ""]
    for tag in tags:
        content = content.replace(f"```{tag}", "")
    return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d", type=str, required=True)
    parser.add_argument("--model", "-m", type=str, required=False, default="gpt-4o-mini")
    parser.add_argument("--start-file", "-s", type=str, required=False, default="")
    args = parser.parse_args()
    ensure_in_flux_branch()
    total_cost, total_time = process_all_blade_files(args.directory, args.model, args.start_file)
    print(f"Total cost: ${total_cost:.6f}")
    print(f"Total time: {total_time:.2f} seconds")
