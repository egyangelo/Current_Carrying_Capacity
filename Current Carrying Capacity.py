# %%
import handcalcs.render
import forallpeople as si
si.environment('default', top_level=True)
handcalcs.set_option("param_columns", 3)
handcalcs.set_option("display_precision", 2)
handcalcs.set_option("decimal_separator", ".")
handcalcs.set_option("line_break", "\\\\[10pt]")
handcalcs.set_option("math_environment_start", "aligned")
handcalcs.set_option("math_environment_end", "aligned")
from math import sin, cos, tan , pi , sqrt

# %% [markdown]
# # 1. Current carrying capacity of a conductor #
# 
# ## 1.1 Reference: ##
# IEEE 605-2008 "Guide of Substation Rigid-Bus Structures"
# 

# %%
# those are the outside and inside diameters of the selected conductor, this should be updated to read from the available list of conductors
#in the futute, I also need to learn how to display the chosed size
D_o = 40 *10**-3 
D_i = 6 *10**-3 
#initial assumptions for the code to work
P_rad = 0
P_conv = 0
P_sol = 0
R_t = 1

#Parameters used for Prad
#Stefan – Boltzmann constant
s =	5.67 * 10**-8
#Emissivity co-efficient for bus
K_e	= 0.5
#Final temperature
T_f	= 358
#Monthly Average ambient temperature
T_a	= 328								

#Parameters used for Pconv
lamb = 0.02585 #Thermal conductivity of the air film in contact with the busbar
V_min = 1 #minimum wind speed
R_e = 1.644E9 * V_min * D_o * ( T_a + 0.5 * ( T_f - T_a))**-1.78 #Reynold's number
N_u = (0.65*(R_e**0.2)) + (0.23*(R_e**0.61))	#Nusselt number

#Parameters used for Psolar
gamma = 0.5 #Solar radiation absorption coefficient						
S_i	= 1000 #Intensity of solar radiation					=	

#The value of the minimum required current
I_req = 100

# %%
%%render 
# symbolic
I_max = sqrt((P_rad + P_conv - P_sol)/R_t)

# %%
%%render
#symbolic
I_max  #Steady State current carrying capacity of the conductor
P_rad  #Radiated Heat Loss
P_conv #Convection Heat Loss
P_sol  #Solar Heat Gain
R_t    #AC Resistance of the conductor at operating tempeature

# %% [markdown]
# # 1.2 Radiated heat loss calculations #

# %%
%%render  sci_not 3

P_rad = s * pi * K_e * D_o * ( T_f**4 - T_a**4 ) 


# %%
%%render
P_rad #Radiated Heat Loss

# %%
%%render sci_not 2

s  #Stefan Boltzmann constant
K_e #Emissivity co-efficient for bus			
T_f #Final temperature					
T_a #Monthly Average ambient temperature of

# %% [markdown]
# # 1.3 Convected heat loss calculations #

# %%
%%render
P_conv = lamb * N_u * pi * (T_f - T_a) 



# %%
%%render sci_not 3
lamb #Thermal conductivity of the air film in contact with the busbar
N_u  #Nusselt number

# %% [markdown]
# # 1.4 Solar radiation hear gain calculations #

# %%
%%render
P_sol	=	gamma * D_o * S_i 						


# %%
%%render sci_not 3
gamma #Solar radiation absorption coefficient						
S_i #Intensity of solar radiation

# %% [markdown]
# # 1.5 AC resistance of the conductor at final temperature #

# %%
# this part is not well constructed in the SEC sheet, I can use the Egyptian sheet instead
R_t = 6.525E-5

# %%

%%render sci_not 3
# long
I_max = sqrt(((P_rad + P_conv - P_sol)/(R_t))) #Amps
           

# %%
if I_max>I_req : 
    Result = "Success, This conductor is sufficient to carry the steady state current"
else :
    Result = "Fail, This conductor is NOT sufficient to carry the steady state current"
    
    



# %%

Result

# %%



