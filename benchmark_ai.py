import subprocess
import time

# AI Implementations
AI_IMPLEMENTATIONS = {
    "Qwen AI (Python)": "python3 run_ai.py",
    "Huobz AI (Python)": "python3 huobz_ai.py",
    "Huobz AI (Assembly)": "nasm -f elf64 huobz_ai.s -o huobz_ai.o && ld -o huobz_ai huobz_ai.o && ./huobz_ai",
    "Huobz AI (C++)": "g++ huobz_ai.cpp -o huobz_ai && ./huobz_ai"
}

def run_benchmark():
    """Runs all AI models and measures execution time."""
    results = {}

    for ai_name, command in AI_IMPLEMENTATIONS.items():
        print(f"\n🚀 Running {ai_name}...\n")
        start_time = time.time()
        
        # Execute the AI command
        process = subprocess.run(command, shell=True, text=True, capture_output=True)
        end_time = time.time()
        
        execution_time = end_time - start_time
        results[ai_name] = execution_time

        print(f"🕒 Execution Time: {execution_time:.4f} seconds\n")
        print(f"⚡ Output:\n{process.stdout}")
        if process.stderr:
            print(f"⚠ Error:\n{process.stderr}")

    # Print Performance Comparison
    print("\n📊 AI Performance Comparison:")
    for ai_name, exec_time in sorted(results.items(), key=lambda x: x[1]):
        print(f"✅ {ai_name}: {exec_time:.4f} seconds")

if __name__ == "__main__":
    run_benchmark()
