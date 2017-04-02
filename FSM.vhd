--Present State Logic
process(clk, rst)
begin 
    if(rst='1') then 
	    state<=S0; 
    elsif(rising_edge(clk)) then
	    state <= next_state;
    end if;
end process;

--Output Logicprocess(state)
begin
   case state is
when S0=>Z<='0'; 
when S1=>Z<='1'; 
end case; 
end process;
 
--Next State Logic
process(state, X)
begin 
   case state is
       when S0 =>
           if(X='00') then
               next_state<=S0;
           end if;
           if(X='01') then
               next_state<=S1;
           end if;
       when S1 =>
           if(X='00') then
               next_state<=S1;
           end if;
           if(X='01') then
               next_state<=S0;
           end if;
   end case;
end process;
-- :3
