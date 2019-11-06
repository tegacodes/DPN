# The Command Line

The command line is a text-based interface for interacting with your computer. From the command line you can launch programs, view files, and manipulate your file system by making, moving, and copying files and directories. You can think of it as the Finder in Mac, without the graphic interface, but much more powerful.

## Setup

On a Mac you can access the command line by opening up the `Terminal` application, located in `/Applications/Utilities/Terminal`

To get started on Windows you will need to set up the Windows Subsystem for Linux, which allows you to run Ubuntu (a Linux distribution) from within your current Windows 10 installation.  [Follow this guide to do so](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows).


## The Prompt

When you open up your terminal application you'll see something like this:

```bash
SamsComputer:~ sam$
```

This is called the "prompt". By default (on a Mac) it shows the name of the computer, the directory that you are currently in, your username, and then a $ sign.

The basic use of the command line is: 1) you type a command, 2) you hit return, and 3) some output of the command is printed to the screen.

## Basic Navigation & File Operations

*Please note I use the word "directory" and "folder" interchangeably.*

When you open a new terminal window, you are placed inside your home folder. On a Mac this is `/Users/myusername` and on Linux, `/home/myusername`. 

To see the folder you are currently in, type: `pwd` and hit return. `pwd` stands for "print working directory", or in other words, "show me the directory I am currently working from".

#### Here are some basic commands for getting around, making, deleting and copying files and folders.


**`pwd`** stands for "print working directory". It prints out where you are:

```bash
pwd
```

**`ls`** stands for "list". It lists the contents of current directory.

```bash
ls
```

**`cd`** stands for "change directory". Type `cd` and then the directory you want to go to. For example, change to the Desktop from your home folder:

```bash
cd Desktop
```

To go into the parent folder, up one level in the file structure, type `..` or `../` instead of a folder name, like so:

```bash
cd ..
```

If you type `cd` without a folder name after, it takes you back to your home folder.


**`mkdir`** stands for "make directory". Type `mkdir` and then a name to make a folder. For example, make a folder called "cool_project":

```bash
mkdir cool_project
```

**`mv`** stands for "move". It lets you move files and folders and also rename them. To rename a file:

```bash
mv oldname.txt newname.txt
```

**`cp`** stands for "copy". It lets duplicate files:

```bash
cp draft.txt draft_copy.txt
```

**`rm`** stands for "remove". It lets you delete files:

```bash
rm bad_selfie.jpg
```

Please note, `rm` will **not** ask for confirmation, and it will not move files to the trash. It'll just delete them immediately, so be careful.

**`cat`** stands for "concatenate" and it shows you the contents of a file and also allows you to join two files together. For example, to print out the entirety of Moby Dick:

```bash
cat mobydick.txt
```

**`more`** is like `cat` but will paginate the output if it is larger than the size of your terminal window:

```bash
more mobydick.txt
```
(now use the up and down arrows to go up or down by a line, the space to go down by a page and `q` to exit if needed)

**`file`** provides basic info about a file:

```bash
file mysterfile.what
```

**`sort`** sorts a file alphabetically by line and prints the output to the screen

```bash
sort names.txt
```

**`grep`** searches each line of a file for some input, and prints those lines to the screen. For example, the following searches for all lines in Moby Dick containing the word "whale".

```bash
grep whale mobydick.txt
```

## Command Line Options and Getting Help

Most commands have extra options that you can input when you run the command.  They are usually preceded by either one or two dashes (`-` or `--`). 

The structure of a typical command looks like this:

```bash
command_name [options] arguments
```

("arguments" refers to the file or files your are running the command with)

For example, the `sort` command outputs in ascending order by default, but you can have it use reverse order with the `-r` option, like so:

```bash
sort -r mobydick.txt
```

You can also tell `sort` to only output unique lines (ie, to remove any duplicate lines) with the `-u` option:

```bash
sort -u mobydick.txt
```

Finally you can combine options:

```bash
sort -u -r mobydick.txt
```

Sometimes, options have parameters. For example, the `cut` command cuts out portions of each line of a file. To use it you must specify a delimiter character with the `-d` option and field number to extract with the `-f` option.  To get the first word of every line in Moby Dick I might enter:

```bash
cut -d " " -f 1 mobydick.txt
```

To see all the options and view a manual for any command, use the `man` tool (short for "manual")

```bash
man cut
```

Use the arrow keys to navigate, and `q` to exit.


## Piping and Directing Output

Most commands will produce output on the screen. However we can also automatically save that output to the filesystem using the `>` character followed by a filename.

Sort a file called "names.txt", and save the output to a new file called "sorted_names.txt":

```bash
sort names.txt > sorted_names.txt
```

`>` will create a file if it does not already exist, or overwrite one if it does. You can use `>>` instead to append to a file.

Unix also has a very powerful concept called "pipes" which allow us to chain commands together, effectively feeding the output of one command into the input of another. To do so, we use the `|` symbol.

Extract all lines of Moby Dick containing "whale", then sort them.

```bash
grep whale mobydick.txt | sort -u
```

The `|` here means "take the output of the grep command and send it to sort -u". You can use as many pipes as you desire, and combine this technique with the output redirection.

Extract all lines of Moby Dick containing "whale", then sort them, then save to a new file called "sorted_whales.txt"

```bash
grep whale mobydick.txt | sort -u > sorted_whales.txt
```


## The Structure of the Filesytem

Everything on your computer is either a file or a folder, and these files and folders are organized hierarchically, like a tree. At the very bottom of the tree is the "root folder", indicated by a single forward slash, like so `/`. Here's a basic example of directory structure:

```
/
	Users/
  		sam/
   			Desktop/
	  			trotsky.jpg
	  			the_man_without_qualities.txt
	 		Documents/
	 		Downloads/			
		Guest/
	Applications/
	Volumes/
```

Each file and folder has a unique location on the filesystem. This location is called a "path". You can reference files and folders either by their **relative** path, or by their **absolute** or **full** path. In the previous examples I have been using the relative path - that is, I have been referencing files relative to where I currently am. **A path is absolute if it begins with a `/`**

For example the absolute path to `the_man_without_qualities.txt` in the above filesystem is `/Users/sam/Desktop/the_man_without_qualities.txt`. I can look inside the contents of this file, from any working directory, with this command:

```bash
more /Users/sam/Desktop/the_man_without_qualities.txt
```

There are a few shortcuts for dealing paths as well. 

`.` (single dot) or './' (single dot with slash) means the current folder that I am in.

`..` (two dots) or `../` (two dots with slash) means the parent folder. For example, if am in my Desktop folder and I want to list the contents of my Downloads folder I could type:

```bash
ls ../Downloads/
``` 

## Wildcards

It's also possible to reference multiple files using the `*` character in combination with other characters. This can be really useful in a lot of situations.

For example, you can list all files that begin with the word "the" like so:

```bash
ls the*
```

List all jpg images:

```bash
ls *.jpg
```

Make a folder called `images` and move all jpeg images into it:

```bash
mkdir images
mv *.jpg images/


```

## Finding and Replacing

You can use the `tr` command to manipulate characters in lines of files.

This will delete all instances of the letter "e"

```bash
"help" | tr -d "e"
```

This will replace instances of "e" with "a".

```bash
echo "help" | tr -s "e" "a"
```

You can also use the `sed` command to find and replace characters.

This will replace all instances of "good" with "bad" in a file.

```bash
sed 's/good/bad/g' filename.txt
```



## Tips

It can take a while to get used to the command line, but there are a few tips and trick that make it much easier to use.

* Use the up and down arrows to view a history of the commands you have entered. 
* Hit the tab key to autocomplete commands and file paths
* Type `open` and then a filename to open the file in its default program
* Drag a folder or file onto the terminal to fill in its absolute path
* Type ctrl-a to move your cursor to the beginning of the line, and ctrl-e to the end