def arithmetic_arranger(problems, solve=None):
      if len(problems) > 5:
          return "Error: Too many problems."

      arranged = {"top": [], "bottom": [], "line": [], "result": []}

      for problem in problems:
          operand1, operator, operand2 = problem.split()

          if len(operand1) >= 5 or len(operand2) >=5:
              return "Error: Numbers cannot be more than four digits."
          if not operand1.isnumeric() or not operand2.isnumeric():
              return "Error: Numbers must only contain digits."
          if operator not in "+-":
              return "Error: Operator must be '+' or '-'."

          max_length = max(len(operand1), len(operand2))
          top_operand = operand1.rjust(max_length + 2)
          bottom_operand = operator + operand2.rjust(max_length + 1)
          line = "-" * (max_length + 2)

          arranged["top"].append(top_operand)
          arranged["bottom"].append(bottom_operand)
          arranged["line"].append(line)

          if solve is True:
              if operator == "+":
                  result = str(int(operand1) + int(operand2))
              else:
                  result = str(int(operand1) - int(operand2))
              arranged["result"].append(result.rjust(max_length + 2))

      arranged_problems = "    ".join(arranged["top"]) + "\n" + "    ".join(
          arranged["bottom"]) + "\n" + "    ".join(arranged["line"])

      if solve is True:
          arranged_problems += "\n" + "    ".join(arranged["result"])

      return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))