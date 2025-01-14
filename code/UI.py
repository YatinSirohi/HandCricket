import tkinter as tk
import random
from PIL import Image, ImageTk
import itertools
import numpy as np
from PIL import Image, ImageTk

class AnimatedGIF(tk.Label):  # For inserting GIF, image, Videos
    def __init__(self, master, path, delay=100, size=(100, 100)):
        super().__init__(master)
        self.delay = delay
        self.frames = []
        self.master = master
        self.size = size  # Store the desired size

        # Open the GIF file
        gif = Image.open(path)
        try:
            while True:
                frame = gif.copy()
                frame = frame.resize(self.size, Image.LANCZOS)  # Resize the frame
                self.frames.append(ImageTk.PhotoImage(frame))
                gif.seek(len(self.frames))  # Move to the next frame
        except EOFError:
            pass

        self.frames_cycle = itertools.cycle(self.frames)
        self.running = False  # Initially set to not running
        self.update_frame()

    def update_frame(self):
        if self.running:
            frame = next(self.frames_cycle)
            self.config(image=frame)
            self.master.after(self.delay, self.update_frame)

    def start_animation(self):
        self.running = True
        self.update_frame()

    def stop_animation(self):
        self.running = False

    def reset_animation(self):
        self.frames_cycle = itertools.cycle(self.frames)
        self.start_animation()


class Commentary:
    def one_run_commentary():
        commentaries = [
            "That's a delicate push into the off side, and they take a quick single to rotate the strike.",
            "A gentle nudge to mid-wicket, and the batsmen hurry through for a well-judged single.",
            "Flicked off the pads down to fine leg, and they stroll through for a comfortable single.",
            "The ball is tapped softly to point, and there's a quick call for a single, safely taken.",
            "Driven gently to cover, and they set off for a single, keeping the scoreboard moving.",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="blue", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label

    def two_run_commentary():
        commentaries = [
            "Nicely played through the covers, and they come back for a comfortable two.",
            "A well-timed shot to the deep mid-wicket boundary, and they manage to run two.",
            "Pushed firmly past the bowler, and the batsmen run hard to collect a couple of runs.",
            "Cut away to deep point, and they make it back for a quick two runs.",
            "A deft flick off the pads towards square leg, and they hurry back for two.",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="blue", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label

    def three_run_commentary():
        commentaries = [
            "Driven through the covers, and they run hard to complete three runs.",
            "A powerful shot to deep mid-wicket, and the batsmen come back for three.",
            "Pushed past the bowler, and they run quickly to collect three runs.",
            "Cut away to deep point, and they manage to take three runs.",
            "Flicked off the pads towards deep square leg, and they rush back for three.",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="blue", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label

    def four_run_commentary():
        commentaries = [
            "What a shot! That's been driven beautifully through the covers for four.",
            "A powerful pull shot, and it's raced away to the boundary for four runs.",
            "A delightful flick off the pads, and the ball races to the boundary for four.",
            "Smashed through point, and it whistles away to the fence for four.",
            "A textbook cover drive, and it pierces the gap for a boundary.",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="orange", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label

    def six_run_commentary():
        commentaries = [
            "That's massive! It's gone all the way for six.",
            "A huge hit, straight out of the ground for six runs!",
            "What a strike! That ball is sailing over the boundary for six.",
            "A towering six, hit with incredible power.",
            "Clears the ropes with ease, that's six runs!",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="yellow", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label

    def wicket_commentary():
        commentaries = [
            "Clean bowled! The stumps are shattered and the batsman has to go.",
            "Caught behind! The bowler gets the edge and the keeper does the rest.",
            "LBW! The umpire's finger goes up, and the batsman is out leg before wicket.",
            "A stunning catch in the outfield! The fielder takes a blinder to send the batsman back.",
            "Bowled him! The ball sneaks through the defense and knocks the stumps over.",
        ]
        chosen_commentary = np.random.choice(commentaries)
        commentary_label = tk.Label(
            root, font=("bold", 15), fg="red", bg="gray", text=chosen_commentary
        )
        commentary_label.pack(pady=10)
        root.after(2500, commentary_label.pack_forget)
        return commentary_label


wickets = (
    []
)  # Save user entered number of wickets - decides for how many wickets game will run


def generateRuns():  # computer generated runs or choices randomly
    runsAvailable = [1, 2, 3, 4, 6]
    run = np.random.choice(runsAvailable, p=[0.2, 0.2, 0.2, 0.2, 0.2])
    return run


def match_reset():  # Reset match at any point
    for widget in root.winfo_children():
        widget.pack_forget()
        reset.pack(anchor="ne", padx=10, pady=10)

    # Add initial widgets back
    greet.pack(pady=20)
    number_of_wicket.pack(pady=5)
    number_of_wicket_entry.delete(0, 'end')
    number_of_wicket_entry.pack(pady=10)
    heads.pack()
    tails.pack()
    start_toss.pack(pady=10)
    reset.pack(anchor="ne", padx=10, pady=10)  # Fix reset top at top right


def user_runs(index):
    runs = [1, 2, 3, 4, 6]
    return int(runs[index])

def validate_number_of_wickets(P):
    if P.isdigit() or P == "":
        return True
    return False
    
def match_simulation():  # User batting first code
    totalUserRuns = tk.IntVar()  # Setting initial score and wickets to 0
    totalUserRuns.set(0)
    userWickets = tk.IntVar()
    userWickets.set(0)
    totalCompRuns = tk.IntVar()
    totalCompRuns.set(0)
    computerWickets = tk.IntVar()
    computerWickets.set(0)

    runs_label = tk.Label(
        root,
        font=("bold", 20),
        text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}",
    )
    runs_lable_comp = tk.Label(
        root,
        font=("bold", 20),
        text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}",
    )
    user_choice_selected_list = [0]
    computer_score_list = [
        0
    ]  # to store the user choice and compare with computer random choice, when user batting first
    user_score_list = []  # keep track of user runs scored

    def check_all_out():
        if int(wickets[0]) == userWickets.get():
            for widget in root.winfo_children():
                widget.pack_forget()
                reset.pack(anchor="ne", padx=10, pady=10)
            # user_choice_selected_list.clear()
            # user_choice_selected_list.append(0)
            tk.Label(root, font=("bold", 20), text="All Out").pack()
            runs_label.pack()
            runs_label.config(
                text=f"Final score is: {totalUserRuns.get()} / {userWickets.get()}"
            )
            second_innings_btn = tk.Button(
                root,
                text="Start 2nd Innings",
                command=second_innings,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
            )
            second_innings_btn.pack(pady=10)

    def check_all_out_comp_innings():  # Check computer 2nd batting innings if its all out and/or won the match
        if int(wickets[0]) == computerWickets.get() or int(totalCompRuns.get()) > int(
            totalUserRuns.get()
        ):
            for widget in root.winfo_children():
                widget.pack_forget()
                reset.pack(anchor="ne", padx=10, pady=10)
            if int(totalCompRuns.get()) < int(totalUserRuns.get()):
                tk.Label(root, font=("bold", 20), text="Computer All Out").pack()
            runs_lable_comp.pack(pady=10)
            runs_lable_comp.config(
                text=f"Computer score: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            runs_label.pack(pady=10)
            runs_label.config(
                text=f"Your score: {totalUserRuns.get()} / {userWickets.get()}"
            )

            if int(totalCompRuns.get()) < int(totalUserRuns.get()):
                tk.Label(
                    root, font=("bold", 20), fg="blue", text="You won the match"
                ).pack(pady=10)

            if int(totalCompRuns.get()) == int(totalUserRuns.get()):
                tk.Label(root, font=("bold", 20), text="Match Tied !!").pack(pady=10)

            if int(totalCompRuns.get()) > int(totalUserRuns.get()):
                tk.Label(
                    root, font=("bold", 20), fg="red", text="Computer won the match"
                ).pack(pady=10)

    # -------------------------------------------------------------------------------------------------------- Functions to add runs ---------------
    def one_run():
        choice_generated = generateRuns()
        user_choice_selected_list.append(1)
        if (
            choice_generated == user_choice_selected_list[-1]
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_wickets = userWickets.get() + 1
            userWickets.set(latest_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            return latest_wickets
        else:
            latest_score = totalUserRuns.get() + 1
            totalUserRuns.set(latest_score)
            user_score_list.append(1)
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            Commentary.one_run_commentary()

            return latest_score

    def two_run():
        choice_generated = generateRuns()
        user_choice_selected_list.append(2)
        if choice_generated == user_choice_selected_list[-1]:
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_wickets = userWickets.get() + 1
            userWickets.set(latest_wickets)
            check_all_out()
            Commentary.wicket_commentary()
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            return latest_wickets
        else:
            latest_score = totalUserRuns.get() + 2
            totalUserRuns.set(latest_score)
            user_score_list.append(2)
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            Commentary.two_run_commentary()

            return latest_score

    def three_run():
        choice_generated = generateRuns()
        user_choice_selected_list.append(3)
        if choice_generated == user_choice_selected_list[-1]:
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_wickets = userWickets.get() + 1
            userWickets.set(latest_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            return latest_wickets
        else:
            latest_score = totalUserRuns.get() + 3
            totalUserRuns.set(latest_score)
            user_score_list.append(3)
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            Commentary.three_run_commentary()

            return latest_score

    def four_run():
        choice_generated = generateRuns()
        user_choice_selected_list.append(4)
        if choice_generated == user_choice_selected_list[-1]:
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_wickets = userWickets.get() + 1
            userWickets.set(latest_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            return latest_wickets
        else:
            latest_score = totalUserRuns.get() + 4
            totalUserRuns.set(latest_score)
            user_score_list.append(4)
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            Commentary.four_run_commentary()
            return latest_score

    def six_run():
        choice_generated = generateRuns()
        user_choice_selected_list.append(6)
        if choice_generated == user_choice_selected_list[-1]:
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_wickets = userWickets.get() + 1
            userWickets.set(latest_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            return latest_wickets
        else:
            latest_score = totalUserRuns.get() + 6
            totalUserRuns.set(latest_score)
            user_score_list.append(6)
            runs_label.config(
                text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
            )
            Commentary.six_run_commentary()
            return latest_score

    if selected_value_batting_bowling.get() == "1":  # User batting code
        for widget in root.winfo_children():
            widget.pack_forget()
            reset.pack(anchor="ne", padx=10, pady=10)
        you_batting_msg = tk.Label(
            root, font=("bold", 20), fg="red", text=f"You are batting"
        )
        you_batting_msg.pack(pady=5)
        # ----------------------------------------------------------- Buttons --------------------------------
        run_one = tk.Button(  # Button for one run
            root,
            text="1",
            command=one_run,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_one.pack()

        run_two = tk.Button(  # Button for one run
            root,
            text="2",
            command=two_run,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_two.pack(pady=5)

        run_three = tk.Button(  # Button for one run
            root,
            text="3",
            command=three_run,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_three.pack(pady=5)

        run_four = tk.Button(  # Button for one run
            root,
            text="4",
            command=four_run,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_four.pack(pady=5)

        run_six = tk.Button(  # Button for one run
            root,
            text="6",
            command=six_run,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_six.pack(pady=5)
        runs_label.pack(pady=10)  # Show score

    # --------------------------------------------------------------------------- Computer batting after user has batted -----------------------------------
    def second_innings():
        for widget in root.winfo_children():
            widget.pack_forget()
            reset.pack(anchor="ne", padx=10, pady=10)

        first_innings_score = tk.Label(
            root,
            font=("bold", 20),
            text=f"1st Innings score: {totalUserRuns.get()} / {userWickets.get()}",
        )
        first_innings_score.pack()
        you_are_bowling_msg = tk.Label(
            root, font=("bold", 20), fg="red", text=f"You are Bowling"
        )
        you_are_bowling_msg.pack(pady=5)

        def one_run_sec_innings():
            choice_generated = generateRuns()
            if (
                choice_generated == 1
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_comp_wickets = computerWickets.get() + 1
                computerWickets.set(latest_comp_wickets)
                Commentary.wicket_commentary()
                check_all_out_comp_innings()
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                return latest_comp_wickets
            else:
                latest_comp_score = totalCompRuns.get() + choice_generated
                computer_score_list.append(choice_generated)
                totalCompRuns.set(latest_comp_score)
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                if choice_generated == 2:
                    Commentary.two_run_commentary()
                if choice_generated == 3:
                    Commentary.three_run_commentary()
                if choice_generated == 4:
                    Commentary.four_run_commentary()
                if choice_generated == 6:
                    Commentary.six_run_commentary()
                runs_needed_calculation = sum(user_score_list) - latest_comp_score
                runs_needed.config(
                    text=f"Computer needs {runs_needed_calculation} runs to win"
                )
                check_all_out_comp_innings()
                return latest_comp_score, runs_needed_calculation

        def two_run_sec_innings():
            choice_generated = generateRuns()
            if (
                choice_generated == 2
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_comp_wickets = computerWickets.get() + 1
                computerWickets.set(latest_comp_wickets)
                Commentary.wicket_commentary()
                check_all_out_comp_innings()
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                return latest_comp_wickets
            else:
                latest_comp_score = totalCompRuns.get() + choice_generated
                computer_score_list.append(choice_generated)
                totalCompRuns.set(latest_comp_score)
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                if choice_generated == 1:
                    Commentary.one_run_commentary()
                if choice_generated == 3:
                    Commentary.three_run_commentary()
                if choice_generated == 4:
                    Commentary.four_run_commentary()
                if choice_generated == 6:
                    Commentary.six_run_commentary()
                runs_needed_calculation = sum(user_score_list) - latest_comp_score
                runs_needed.config(
                    text=f"Computer needs {runs_needed_calculation} runs to win"
                )
                check_all_out_comp_innings()
                return latest_comp_score, runs_needed_calculation

        def three_run_sec_innings():
            choice_generated = generateRuns()
            if (
                choice_generated == 3
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_comp_wickets = computerWickets.get() + 1
                computerWickets.set(latest_comp_wickets)
                Commentary.wicket_commentary()
                check_all_out_comp_innings()
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                return latest_comp_wickets
            else:
                latest_comp_score = totalCompRuns.get() + choice_generated
                computer_score_list.append(choice_generated)
                totalCompRuns.set(latest_comp_score)
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                if choice_generated == 1:
                    Commentary.one_run_commentary()
                if choice_generated == 2:
                    Commentary.two_run_commentary()
                if choice_generated == 4:
                    Commentary.four_run_commentary()
                if choice_generated == 6:
                    Commentary.six_run_commentary()
                runs_needed_calculation = sum(user_score_list) - latest_comp_score
                runs_needed.config(
                    text=f"Computer needs {runs_needed_calculation} runs to win"
                )
                check_all_out_comp_innings()
                return latest_comp_score, runs_needed_calculation

        def four_run_sec_innings():
            choice_generated = generateRuns()
            if (
                choice_generated == 4
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_comp_wickets = computerWickets.get() + 1
                computerWickets.set(latest_comp_wickets)
                Commentary.wicket_commentary()
                check_all_out_comp_innings()
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                return latest_comp_wickets
            else:
                latest_comp_score = totalCompRuns.get() + choice_generated
                computer_score_list.append(choice_generated)
                totalCompRuns.set(latest_comp_score)
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                if choice_generated == 1:
                    Commentary.one_run_commentary()
                if choice_generated == 2:
                    Commentary.two_run_commentary()
                if choice_generated == 3:
                    Commentary.three_run_commentary()
                if choice_generated == 6:
                    Commentary.six_run_commentary()
                runs_needed_calculation = sum(user_score_list) - latest_comp_score
                runs_needed.config(
                    text=f"Computer needs {runs_needed_calculation} runs to win"
                )
                check_all_out_comp_innings()
                return latest_comp_score, runs_needed_calculation

        def six_run_sec_innings():
            choice_generated = generateRuns()
            if (
                choice_generated == 6
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_comp_wickets = computerWickets.get() + 1
                computerWickets.set(latest_comp_wickets)
                Commentary.wicket_commentary()
                check_all_out_comp_innings()
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                return latest_comp_wickets
            else:
                latest_comp_score = totalCompRuns.get() + choice_generated
                computer_score_list.append(choice_generated)
                totalCompRuns.set(latest_comp_score)
                runs_lable_comp.config(
                    text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
                )
                if choice_generated == 1:
                    Commentary.one_run_commentary()
                if choice_generated == 2:
                    Commentary.two_run_commentary()
                if choice_generated == 3:
                    Commentary.three_run_commentary()
                if choice_generated == 4:
                    Commentary.four_run_commentary()
                runs_needed_calculation = sum(user_score_list) - latest_comp_score
                runs_needed.config(
                    text=f"Computer needs {runs_needed_calculation} runs to win"
                )
                check_all_out_comp_innings()
                return latest_comp_score, runs_needed_calculation

        run_one_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="1",
            command=one_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_one_sec_innings.pack()

        run_two_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="2",
            command=two_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_two_sec_innings.pack(pady=5)

        run_three_sec_innings = (
            tk.Button(  # Button for one run 2nd innings after batting
                root,
                text="3",
                command=three_run_sec_innings,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
                width=10,
            )
        )
        run_three_sec_innings.pack(pady=5)

        run_four_sec_innings = (
            tk.Button(  # Button for one run 2nd innings after batting
                root,
                text="4",
                command=four_run_sec_innings,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
                width=10,
            )
        )
        run_four_sec_innings.pack(pady=5)

        run_six_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="6",
            command=six_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_six_sec_innings.pack(pady=5)
        runs_lable_comp.pack(pady=5)
        # wickets_left = int(wickets[0]) - computerWickets.get()
        runs_needed = tk.Label(
            root,
            font=("bold", 20),
            fg="blue",
            text=f"Computer needs {totalUserRuns.get()} runs to win",
        )
        runs_needed.pack(pady=10)

    # ------------------------------------------------------------- Below function when user chooses bowling--------------------------------------------

    if (
        selected_value_batting_bowling.get() == "2"
    ):  # User bowling first - run match_simulation_bowling_first function
        match_simulation_bowling_first()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def match_simulation_bowling_first():  # User bowling first code
    for widget in root.winfo_children():
        widget.pack_forget()
        reset.pack(anchor="ne", padx=10, pady=10)
    tk.Label(root, font=("bold", 20), fg="red", text="You are Bowling").pack()
    totalUserRuns = tk.IntVar()  # Setting initial score and wickets to 0
    totalUserRuns.set(0)
    userWickets = tk.IntVar()
    userWickets.set(0)
    totalCompRuns = tk.IntVar()
    totalCompRuns.set(0)
    computerWickets = tk.IntVar()
    computerWickets.set(0)
    runs_label = tk.Label(
        root,
        font=("bold", 20),
        text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}",
    )
    runs_lable_comp = tk.Label(
        root,
        font=("bold", 20),
        text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}",
    )
    user_choice_selected_list = [0]
    computer_score_list = [
        0
    ]  # to store the user choice and compare with computer random choice, when user batting first
    user_score_list = []

    def check_all_out():
        if int(wickets[0]) == computerWickets.get():
            for widget in root.winfo_children():
                widget.pack_forget()
                reset.pack(anchor="ne", padx=10, pady=10)
            # user_choice_selected_list.clear()
            # user_choice_selected_list.append(0)
            tk.Label(root, font=("bold", 20), text="Computer All Out").pack()
            runs_lable_comp.pack()
            runs_lable_comp.config(
                text=f"Computer final score is: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            second_innings_btn = tk.Button(
                root,
                text="Start 2nd Innings",
                command=second_innings_user,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
            )
            second_innings_btn.pack(pady=10)

    def check_all_out_user_innings():  # Check computer 2nd batting innings if its all out and/or won the match
        if int(wickets[0]) == userWickets.get() or int(totalUserRuns.get()) > int(
            totalCompRuns.get()
        ):
            for widget in root.winfo_children():
                widget.pack_forget()
                reset.pack(anchor="ne", padx=10, pady=10)
                runs_label.pack(pady=10)
            if int(totalUserRuns.get()) < int(totalCompRuns.get()):
                tk.Label(root, font=("bold", 20), text="All Out").pack()
            runs_lable_comp.pack(pady=10)
            runs_lable_comp.config(
                text=f"Computer score: {totalCompRuns.get()} / {computerWickets.get()}"
            )

            runs_label.config(
                text=f"Your score: {totalUserRuns.get()} / {userWickets.get()}"
            )

            if int(totalCompRuns.get()) < int(totalUserRuns.get()):
                tk.Label(
                    root, font=("bold", 20), fg="blue", text="You won the match"
                ).pack(pady=10)

            if int(totalCompRuns.get()) == int(totalUserRuns.get()):
                tk.Label(root, font=("bold", 20), text="Match Tied !!").pack(pady=10)

            if int(totalCompRuns.get()) > int(totalUserRuns.get()):
                tk.Label(
                    root, font=("bold", 20), fg="red", text="Computer won the match"
                ).pack(pady=10)

    def one_run():
        choice_generated = generateRuns()
        if (
            choice_generated == 1
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_comp_wickets = computerWickets.get() + 1
            computerWickets.set(latest_comp_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            return latest_comp_wickets
        else:
            latest_comp_score = totalCompRuns.get() + choice_generated
            computer_score_list.append(choice_generated)
            totalCompRuns.set(latest_comp_score)
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            if choice_generated == 2:
                Commentary.two_run_commentary()
            if choice_generated == 3:
                Commentary.three_run_commentary()
            if choice_generated == 4:
                Commentary.four_run_commentary()
            if choice_generated == 6:
                Commentary.six_run_commentary()
            return latest_comp_score

    def two_run():
        choice_generated = generateRuns()
        if (
            choice_generated == 2
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_comp_wickets = computerWickets.get() + 1
            computerWickets.set(latest_comp_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            return latest_comp_wickets
        else:
            latest_comp_score = totalCompRuns.get() + choice_generated
            computer_score_list.append(choice_generated)
            totalCompRuns.set(latest_comp_score)
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            if choice_generated == 1:
                Commentary.one_run_commentary()
            if choice_generated == 3:
                Commentary.three_run_commentary()
            if choice_generated == 4:
                Commentary.four_run_commentary()
            if choice_generated == 6:
                Commentary.six_run_commentary()
            return latest_comp_score

    def three_run():
        choice_generated = generateRuns()
        if (
            choice_generated == 3
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_comp_wickets = computerWickets.get() + 1
            computerWickets.set(latest_comp_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            return latest_comp_wickets
        else:
            latest_comp_score = totalCompRuns.get() + choice_generated
            computer_score_list.append(choice_generated)
            totalCompRuns.set(latest_comp_score)
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            if choice_generated == 1:
                Commentary.one_run_commentary()
            if choice_generated == 2:
                Commentary.two_run_commentary()
            if choice_generated == 4:
                Commentary.four_run_commentary()
            if choice_generated == 6:
                Commentary.six_run_commentary()
            return latest_comp_score

    def four_run():
        choice_generated = generateRuns()
        if (
            choice_generated == 4
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_comp_wickets = computerWickets.get() + 1
            computerWickets.set(latest_comp_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            return latest_comp_wickets
        else:
            latest_comp_score = totalCompRuns.get() + choice_generated
            computer_score_list.append(choice_generated)
            totalCompRuns.set(latest_comp_score)
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            if choice_generated == 1:
                Commentary.one_run_commentary()
            if choice_generated == 2:
                Commentary.two_run_commentary()
            if choice_generated == 3:
                Commentary.three_run_commentary()
            if choice_generated == 6:
                Commentary.six_run_commentary()
            return latest_comp_score

    def six_run():
        choice_generated = generateRuns()
        if (
            choice_generated == 6
        ):  # To check if random number equals user number and adding a wicket
            gif_label_bowled.pack()
            gif_label_bowled.start_animation()
            root.after(2000, gif_label_bowled.reset_animation)
            root.after(2000, gif_label_bowled.stop_animation)
            root.after(2000, gif_label_bowled.pack_forget)

            latest_comp_wickets = computerWickets.get() + 1
            computerWickets.set(latest_comp_wickets)
            Commentary.wicket_commentary()
            check_all_out()
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            return latest_comp_wickets
        else:
            latest_comp_score = totalCompRuns.get() + choice_generated
            computer_score_list.append(choice_generated)
            totalCompRuns.set(latest_comp_score)
            runs_lable_comp.config(
                text=f"Total Computer Runs: {totalCompRuns.get()} / {computerWickets.get()}"
            )
            if choice_generated == 1:
                Commentary.one_run_commentary()
            if choice_generated == 2:
                Commentary.two_run_commentary()
            if choice_generated == 3:
                Commentary.three_run_commentary()
            if choice_generated == 4:
                Commentary.four_run_commentary()

            return latest_comp_score

    run_one = tk.Button(  # Button for one run
        root,
        text="1",
        command=one_run,
        font=("Arial", 15),
        activebackground="gray",
        cursor="hand2",
        bg="lightblue",
        fg="black",
        width=10,
    )
    run_one.pack()

    run_two = tk.Button(  # Button for one run
        root,
        text="2",
        command=two_run,
        font=("Arial", 15),
        activebackground="gray",
        cursor="hand2",
        bg="lightblue",
        fg="black",
        width=10,
    )
    run_two.pack(pady=5)

    run_three = tk.Button(  # Button for one run
        root,
        text="3",
        command=three_run,
        font=("Arial", 15),
        activebackground="gray",
        cursor="hand2",
        bg="lightblue",
        fg="black",
        width=10,
    )
    run_three.pack(pady=5)

    run_four = tk.Button(  # Button for one run
        root,
        text="4",
        command=four_run,
        font=("Arial", 15),
        activebackground="gray",
        cursor="hand2",
        bg="lightblue",
        fg="black",
        width=10,
    )
    run_four.pack(pady=5)

    run_six = tk.Button(  # Button for one run
        root,
        text="6",
        command=six_run,
        font=("Arial", 15),
        activebackground="gray",
        cursor="hand2",
        bg="lightblue",
        fg="black",
        width=10,
    )
    run_six.pack(pady=5)

    runs_lable_comp.pack(pady=5)

    def second_innings_user():  # 2nd innings - user batting code
        for widget in root.winfo_children():
            widget.pack_forget()
            reset.pack(anchor="ne", padx=10, pady=10)
        first_innings_score = tk.Label(
            root,
            font=("bold", 20),
            text=f"1st Innings score: {totalCompRuns.get()} / {computerWickets.get()}",
        )
        first_innings_score.pack()
        you_are_batting_msg = tk.Label(
            root, font=("bold", 20), fg="red", text=f"You are Batting"
        )
        you_are_batting_msg.pack(pady=5)

        def one_run_sec_innings():
            choice_generated = generateRuns()
            user_choice_selected_list.append(1)
            if (
                choice_generated == user_choice_selected_list[-1]
            ):  # To check if random number equals user number and adding a wicket
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_wickets = userWickets.get() + 1
                userWickets.set(latest_wickets)
                Commentary.wicket_commentary()
                check_all_out_user_innings()
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                return latest_wickets
            else:
                latest_score = totalUserRuns.get() + 1
                totalUserRuns.set(latest_score)
                user_score_list.append(1)
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                Commentary.one_run_commentary()
                runs_needed_calculation = (totalCompRuns.get() + 1) - latest_score
                runs_needed.config(
                    text=f"You need {runs_needed_calculation} runs to win"
                )
                check_all_out_user_innings()
                return latest_score

        def two_run_sec_innings():
            choice_generated = generateRuns()
            user_choice_selected_list.append(2)
            if choice_generated == user_choice_selected_list[-1]:
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_wickets = userWickets.get() + 1
                userWickets.set(latest_wickets)
                Commentary.wicket_commentary()
                check_all_out_user_innings()
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                return latest_wickets
            else:
                latest_score = totalUserRuns.get() + 2
                totalUserRuns.set(latest_score)
                user_score_list.append(2)
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                Commentary.two_run_commentary()
                runs_needed_calculation = (totalCompRuns.get() + 1) - latest_score
                runs_needed.config(
                    text=f"You need {runs_needed_calculation} runs to win"
                )
                check_all_out_user_innings()
                return latest_score

        def three_run_sec_innings():
            choice_generated = generateRuns()
            user_choice_selected_list.append(3)
            if choice_generated == user_choice_selected_list[-1]:
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_wickets = userWickets.get() + 1
                userWickets.set(latest_wickets)
                Commentary.wicket_commentary()
                check_all_out_user_innings()
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                return latest_wickets
            else:
                latest_score = totalUserRuns.get() + 3
                totalUserRuns.set(latest_score)
                user_score_list.append(3)
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                Commentary.three_run_commentary()
                runs_needed_calculation = (totalCompRuns.get() + 1) - latest_score
                runs_needed.config(
                    text=f"You need {runs_needed_calculation} runs to win"
                )
                check_all_out_user_innings()
                return latest_score

        def four_run_sec_innings():
            choice_generated = generateRuns()
            user_choice_selected_list.append(4)
            if choice_generated == user_choice_selected_list[-1]:
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_wickets = userWickets.get() + 1
                userWickets.set(latest_wickets)
                Commentary.wicket_commentary()
                check_all_out_user_innings()
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                return latest_wickets
            else:
                latest_score = totalUserRuns.get() + 4
                totalUserRuns.set(latest_score)
                user_score_list.append(4)
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                Commentary.four_run_commentary()
                runs_needed_calculation = (totalCompRuns.get() + 1) - latest_score
                runs_needed.config(
                    text=f"You need {runs_needed_calculation} runs to win"
                )
                check_all_out_user_innings()
                return latest_score

        def six_run_sec_innings():
            choice_generated = generateRuns()
            user_choice_selected_list.append(6)
            if choice_generated == user_choice_selected_list[-1]:
                gif_label_bowled.pack()
                gif_label_bowled.start_animation()
                root.after(2000, gif_label_bowled.reset_animation)
                root.after(2000, gif_label_bowled.stop_animation)
                root.after(2000, gif_label_bowled.pack_forget)

                latest_wickets = userWickets.get() + 1
                userWickets.set(latest_wickets)
                Commentary.wicket_commentary()
                check_all_out_user_innings()
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                return latest_wickets
            else:
                latest_score = totalUserRuns.get() + 6
                totalUserRuns.set(latest_score)
                user_score_list.append(6)
                runs_label.config(
                    text=f"Total Runs: {totalUserRuns.get()} / {userWickets.get()}"
                )
                Commentary.six_run_commentary()
                runs_needed_calculation = (totalCompRuns.get() + 1) - latest_score
                runs_needed.config(
                    text=f"You need {runs_needed_calculation} runs to win"
                )
                check_all_out_user_innings()
                return latest_score

        run_one_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="1",
            command=one_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_one_sec_innings.pack()

        run_two_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="2",
            command=two_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_two_sec_innings.pack(pady=5)

        run_three_sec_innings = (
            tk.Button(  # Button for one run 2nd innings after batting
                root,
                text="3",
                command=three_run_sec_innings,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
                width=10,
            )
        )
        run_three_sec_innings.pack(pady=5)

        run_four_sec_innings = (
            tk.Button(  # Button for one run 2nd innings after batting
                root,
                text="4",
                command=four_run_sec_innings,
                font=("Arial", 15),
                activebackground="gray",
                cursor="hand2",
                bg="lightblue",
                fg="black",
                width=10,
            )
        )
        run_four_sec_innings.pack(pady=5)

        run_six_sec_innings = tk.Button(  # Button for one run 2nd innings after batting
            root,
            text="6",
            command=six_run_sec_innings,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
            width=10,
        )
        run_six_sec_innings.pack(pady=5)
        runs_label.pack(pady=5)
        # wickets_left = int(wickets[0]) - computerWickets.get()
        runs_needed = tk.Label(
            root,
            font=("bold", 20),
            fg="blue",
            text=f"You need {(totalCompRuns.get() + 1)} runs to win",
        )
        runs_needed.pack(pady=10)


# ------------------------------------------------------------------------------------------------------------------------------------


def match_simulation_computer_toss_win():  # when computer wins the toss and chooses batting
    for widget in root.winfo_children():
        widget.pack_forget()
        reset.pack(anchor="ne", padx=10, pady=10)
    match_simulation_bowling_first()


def validate_toss():
    wicket_value = number_of_wicket_entry.get()
    wickets.append(wicket_value)
    if wicket_value:
        computerTossChoice = np.random.choice(["heads", "tails"], p=[0.5, 0.5])
        toss_value = selected_value.get()
        # choose_batting = tk.Radiobutton(
        #     root, variable=selected_value_batting_bowling, text="Batting", value="Batting"
        # )
        # choose_bowling = tk.Radiobutton(
        #     root, variable=selected_value_batting_bowling, text="Bowling", value="Bowling"
        # )

        if toss_value == computerTossChoice:
            user_won_toss = tk.Label(
                root, text="You won the toss. Choose batting or bowling."
            )
            choose_batting = tk.Radiobutton(
                root,
                variable=selected_value_batting_bowling,
                text="Batting",
                value="1",
            )
            choose_bowling = tk.Radiobutton(
                root,
                variable=selected_value_batting_bowling,
                text="Bowling",
                value="2",
            )
            user_won_toss.pack()
            choose_batting.pack(pady=5)
            choose_bowling.pack()

            number_of_wicket.pack_forget()
            number_of_wicket_entry.pack_forget()
            heads.pack_forget()
            tails.pack_forget()
            start_toss.pack_forget()

        start_match_btn = tk.Button(
            root,
            text="START MATCH",
            command=match_simulation,
            font=("Arial", 15),
            activebackground="gray",
            cursor="hand2",
            bg="lightblue",
            fg="black",
        )
        start_match_btn.pack(pady=15)

        if toss_value != computerTossChoice:  # Computer batting first
            user_lost_toss = tk.Label(
                root, text="You lost the toss. Computer is batting.", font=("bold", 20)
            )
            user_lost_toss.pack()
            number_of_wicket.pack_forget()
            number_of_wicket_entry.pack_forget()
            heads.pack_forget()
            tails.pack_forget()
            start_toss.pack_forget()
            start_match_btn.pack_forget()  # Unpack start match button that comes when user wins the toss

            start_match_btn_computer_batting = (
                tk.Button(  # And show button to trigger Computer batting first
                    root,
                    text="START MATCH",
                    command=match_simulation_computer_toss_win,
                    font=("Arial", 15),
                    activebackground="gray",
                    cursor="hand2",
                    bg="lightblue",
                    fg="black",
                )
            )
            start_match_btn_computer_batting.pack(pady=15)

    else:
        input_warning_msg = tk.Toplevel(root)
        input_warning_msg.geometry("300x100")
        input_warning_msg.title("WARNING")
        msg2 = tk.Label(input_warning_msg, text="Number of wickets is mandatory.")
        msg2.pack()


# root details
root = tk.Tk()
root.title("HAND CRICKET BY YATIN SIROHI")
root.geometry("800x600")

# for toss radion buttons
selected_value = tk.StringVar(
    value="heads"
)  # default value for toss redio buttun is set to heads

selected_value_batting_bowling = tk.StringVar(value="3")

vcmd = (root.register(validate_number_of_wickets), '%P')

# entry widget details
number_of_wicket_entry = tk.Entry(root, validate='key', validatecommand=vcmd, text="Number of wickets")

# Root label details
greet = tk.Label(
    root, fg="blue", font=("bold"), justify=tk.CENTER, text="Welcome to hand cricket !!"
)
number_of_wicket = tk.Label(root, font=("bold"), text="Enter number of wickets")

# toss values with radio buttons
heads = tk.Radiobutton(root, variable=selected_value, text="Heads", value="heads")
tails = tk.Radiobutton(root, variable=selected_value, text="Tails", value="tails")

# Gif details
gif_path_bowled = "bowled.gif"
gif_label_bowled = AnimatedGIF(root, gif_path_bowled, delay=100, size=(100, 100))

# buttons
start_toss = tk.Button(
    root,
    text="TOSS",
    command=validate_toss,
    font=("Arial", 15),
    activebackground="gray",
    cursor="hand2",
    bg="lightblue",
    fg="black",
)
reset = tk.Button(
    root,
    text="NEW MATCH",
    command=match_reset,
    font=("Arial", 10, "bold"),
    activebackground="red",
    cursor="hand2",
    bg="yellow",
    fg="black",
)
reset.pack(anchor="ne", padx=10, pady=10)

# Packing widgets
greet.pack(pady=20)
number_of_wicket.pack(pady=5)
number_of_wicket_entry.pack(pady=10)
heads.pack()
tails.pack()
start_toss.pack(pady=10)

root.mainloop()
