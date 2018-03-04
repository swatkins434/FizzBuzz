with Ada.Text_IO;
use Ada.Text_IO;

with Ada.Strings.Unbounded;
use Ada.Strings.Unbounded;

procedure FizzBuzz is
    function GetOutput (N : Positive) return Unbounded_String is
        output : Unbounded_String := To_Unbounded_String("");
    begin -- GetOutput
        if (N mod 3) = 0 then
            Append(output, "fizz");
        end if;

        if (N mod 5) = 0 then
            Append(output, "buzz");
        end if;

        if (output = "") then
            Append(output, Integer'Image(N));
        end if;

        return output;
    end GetOutput;
begin -- FizzBuzz
    for i in 1 .. 100 loop
        Put_Line(To_String(GetOutput(i)));
    end loop;
end FizzBuzz;
