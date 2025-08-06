#!/usr/bin/env python3
"""
Audio-Engleza: Publish script

Commits all changes and pushes to GitHub Pages for deployment.
Use this after generating lessons and updating the HTML index.

Usage:
    python publish.py
    python publish.py --message "Add new hello lesson"
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime

# Configuration  
WEBSITE_DIR = os.getcwd()  # Use current working directory

def run_git_command(command, cwd=None):
    """Run a git command and return the result"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd or WEBSITE_DIR,
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {command}")
        print(f"Error: {e.stderr}")
        return None, e.stderr

def check_git_status():
    """Check if there are changes to commit"""
    stdout, stderr = run_git_command("git status --porcelain")
    if stdout is None:
        return False, []
    
    if not stdout.strip():
        return False, []
    
    # Parse changed files
    changed_files = []
    for line in stdout.strip().split('\n'):
        if line.strip():
            status = line[:2]
            filename = line[3:]
            changed_files.append(f"{status.strip()} {filename}")
    
    return True, changed_files

def commit_and_push(commit_message):
    """Commit all changes and push to GitHub"""
    
    print("🔄 Checking for changes...")
    has_changes, changed_files = check_git_status()
    
    if not has_changes:
        print("✅ No changes to commit. Everything is up to date!")
        return True
    
    print(f"📝 Found {len(changed_files)} changed files:")
    for file_change in changed_files:
        print(f"   {file_change}")
    
    print(f"\n🔄 Adding all changes...")
    stdout, stderr = run_git_command("git add -A")
    if stdout is None:
        print("❌ Failed to add files")
        return False
    
    print(f"💾 Committing with message: {commit_message}")
    escaped_message = commit_message.replace('"', '\\"')
    commit_cmd = f'git commit -m "{escaped_message}"'
    stdout, stderr = run_git_command(commit_cmd)
    if stdout is None:
        print("❌ Failed to commit changes")
        return False
    
    print(f"📤 Pushing to GitHub...")
    stdout, stderr = run_git_command("git push origin main")
    if stdout is None:
        # Try 'master' as fallback
        print("🔄 Trying 'master' branch...")
        stdout, stderr = run_git_command("git push origin master")
        if stdout is None:
            print("❌ Failed to push to GitHub")
            return False
    
    print("✅ Successfully published to GitHub Pages!")
    return True

def get_current_branch():
    """Get the current git branch"""
    stdout, stderr = run_git_command("git branch --show-current")
    if stdout is None:
        return "unknown"
    return stdout or "unknown"

def show_status():
    """Show current git status"""
    print("📊 Current Status:")
    print(f"   Directory: {WEBSITE_DIR}")
    
    branch = get_current_branch()
    print(f"   Branch: {branch}")
    
    has_changes, changed_files = check_git_status()
    if has_changes:
        print(f"   Changes: {len(changed_files)} files modified")
    else:
        print("   Changes: None (clean working tree)")
    
    # Show last commit
    stdout, stderr = run_git_command("git log -1 --oneline")
    if stdout:
        print(f"   Last commit: {stdout}")

def main():
    parser = argparse.ArgumentParser(description='Publish audio-engleza lessons to GitHub Pages')
    parser.add_argument('--message', '-m', 
                       help='Commit message (auto-generated if not provided)')
    parser.add_argument('--status', '-s', action='store_true',
                       help='Show git status and exit')
    
    args = parser.parse_args()
    
    print("\n" + "="*60)
    print("AUDIO-ENGLEZA: Publisher")
    print("Commit and push to GitHub Pages")
    print("="*60)
    
    # Check if we're in the right directory
    if not os.path.exists(WEBSITE_DIR):
        print(f"❌ Website directory not found: {WEBSITE_DIR}")
        sys.exit(1)
    
    if not os.path.exists(os.path.join(WEBSITE_DIR, ".git")):
        print(f"❌ Not a git repository: {WEBSITE_DIR}")
        sys.exit(1)
    
    # Show status if requested
    if args.status:
        show_status()
        sys.exit(0)
    
    # Generate commit message if not provided
    if not args.message:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        args.message = f"Update lessons - {timestamp}\n\n🤖 Generated with [Claude Code](https://claude.ai/code)\n\nCo-Authored-By: Claude <noreply@anthropic.com>"
    
    # Show current status
    show_status()
    print()
    
    # Commit and push
    success = commit_and_push(args.message)
    
    if success:
        print("\n🎉 Lessons published successfully!")
        print("🌐 Your lessons are now live on GitHub Pages")
        print(f"📱 Available at: https://audio-engleza.github.io")
        sys.exit(0)
    else:
        print("\n❌ Publishing failed")
        sys.exit(1)

if __name__ == "__main__":
    main()