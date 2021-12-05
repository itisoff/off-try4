from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail, Details_of_Entry, Pricing
import math

def home(request):
    return render(request, 'start/home.html')

def automated_consultancy(request):
    return render(request, 'start/automated_consultancy.html')

def estimated_cost(request):
    if request.method == 'POST':
        types = int(request.POST.get('type'))
        purpose =int(request.POST.get('purpose'))
        quantity = int(request.POST.get('quantity'))
        length = int(request.POST.get('x'))
        width = int(request.POST.get('y'))
        depth = int(request.POST.get('z'))
        budget = int(request.POST.get('budget'))
        
        print(types,purpose, budget, quantity, length, width, depth)
        
        if(types==1):
            #1A (Corporate Gifts + Budget Friendly), Art paper 120 + Gloss lamination = sheet cost 8tk, size 23x36, gloss lam = 0.005*sq inch*quantity
            if(purpose==1):
                if(budget==1):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #10
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 8 #4000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.005 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 11,201 - 12,662tk
            # 1B (Corporate gifts + Best Rated), Korean Liner 170 + NO Lamination = sheet cost 10, size 29x40, NO lam
            if(purpose==1):
                if(budget==2):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(40/maxx) # 2
                    sheet_w = math.floor(29/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 10 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.00
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0 #0.005 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 10,001 - 11,310 tk

            # 1C (Corporate gifts + Moderately Priced), Art Paoer 170 + Matte Lamination = sheet cost 10, size 23x36, Matte lam = 0.008*sq inch*quantity
            if(purpose==1):
                if(budget==3):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 10 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk
            
            # 1D (Corporate gifts + Good Quality), Swedish Board 300 + Spot Lamination = sheet cost 30, size 44x28, Spot lam = 0.012*sq inch*quantity
            if(purpose==1):
                if(budget==4):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(44/maxx) # 3
                    sheet_w = math.floor(28/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 30 #9990tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.012 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 19,727.1 - 22,300.2 tk


            # 1E (Corporate gifts + Exotic), Swedish Board 350 + Spot Lamination = sheet cost 35, size 44x28, spot lam = 0.012*sq inch*quantity
            if(purpose==1):
                if(budget==5):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(44/maxx) # 3
                    sheet_w = math.floor(28/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 35 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.012 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 21,066.85 - 23,814.7 tk


            # 2A (HR + Budget Friendly), Offset 150 + NO Lamination = sheet cost 5, size 23x36, NO lam
            if(purpose==2):
                if(budget==1):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 5 #2500tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0 #0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 7,705 - 8,710 tk
        
            # 2B (HR + Best Rated), Art Paoer 120 + Glossy Lamination = sheet cost 8, size 23x36, Glossy lam = 0.005*sq inch*quantity
            if(purpose==2):
                if(budget==2):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 8 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.005 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 2C (HR + Moderately Priced), Art Paoer 150 + Matte Lamination = sheet cost 9, size 23x36, Matte lam = 0.008*sq inch*quantity
            if(purpose==2):
                if(budget==3):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 9 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 2D (HR + Good Quality), Art card 300 + Matte Lamination = sheet cost 15, size 22x28, Matte lam = 0.008*sq inch*quantity
            if(purpose==2):
                if(budget==4):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(28/maxx) # 2
                    sheet_w = math.floor(22/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 15 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 2E (HR + Exotic), Art Card 350 + spot Lamination = sheet cost 18, size 22x28, spot lam = 0.012*sq inch*quantity
            if(purpose==2):
                if(budget==5):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(28/maxx) # 2
                    sheet_w = math.floor(22/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 18 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.012 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 3A (Packaging + Budget Friendly), Deshi Liner 120 + No Lamination = sheet cost 5, size 29x40, NO lam
            if(purpose==3):
                if(budget==1):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(40/maxx) # 2
                    sheet_w = math.floor(29/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 5 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.00
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0 #0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 3B (Packaging + Best Rated), Deshi Liner 150 + No Lamination = sheet cost 7, size 29x40, NO lam 
            if(purpose==3):
                if(budget==2):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(40/maxx) # 2
                    sheet_w = math.floor(29/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 7 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.00
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0 #0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 3C (Packaging + Moderately Priced), Korean Liner 150 + NO Lamination = sheet cost 9, size 29x40, No lam 
            if(purpose==3):
                if(budget==3):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(40/maxx) # 2
                    sheet_w = math.floor(29/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 9 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.00
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0 #0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 3D (Packaging + Good Quality), Art Paoer 150 + Matte Lamination = sheet cost 9, size 23x36, Matte lam = 0.008*sq inch*quantity
            if(purpose==3):
                if(budget==4):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(36/maxx) # 2
                    sheet_w = math.floor(23/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 9 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 2.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.008 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

            # 3E (Packaging + Exotic), Sedish Board 300 + Spot Lamination = sheet cost 30, size 44x28, Spot lam = 0.012*sq inch*quantity
            if(purpose==3):
                if(budget==5):
                    # l = 10, w = 6, d = 3
                    x0 = length + depth + 1 #14
                    y0 = width + depth + 1 + 1 #11
                    maxx = max(x0, y0) 
                    minn = min(x0, y0) 
                    sheet_l = math.floor(44/maxx) # 2
                    sheet_w = math.floor(28/minn) # 2
                    tot_cut_1_sheet = sheet_l*sheet_w # 4
                    bags_1sheet = math.floor(tot_cut_1_sheet/2) # 2
                    tot_piece_sheet = math.floor(quantity / bags_1sheet) # q = 1000, tot = 500
                    tot_sheet_price = tot_piece_sheet * 30 #5000tk.........
                
                    # GTO = 14x20, Demi = 18x23, double demi = 26x36
                    machine = 800
                    plate = 400
                    machine_plate = machine + plate # 1200...............

                    #Making cost 29x40 = 2.50, 23x36 = 3.00, 28x44 = 3.50
                    making_cost_per = 3.50
                    tot_making_cost = making_cost_per * quantity #.......

                    lamination = 0.012 * (maxx*minn) * quantity * 2 #.........

                    tot = tot_sheet_price + machine_plate + tot_making_cost + lamination

                    tot_risk1 = tot + (0.15*tot)
                    tot_risk2 = tot + (0.3*tot)


                    print(maxx, minn, sheet_l, sheet_w, tot_sheet_price, machine_plate, tot_making_cost, lamination)
                    #Result = 13,413.6 - 15,163.2 tk

        context = {
            # 'v': v,
            's1': tot_risk1,
            's2': tot_risk2,
        }
        new = Detail(type=types, purpose= purpose, quantity=quantity, length=length, width=width, depth=depth, budget=budget, price1=tot_risk1, price2=tot_risk2)
        new.save()
        new2 = Pricing(type=types, purpose=purpose, budget=budget)
        new2.save()
        return render(request, 'start/estimated_cost.html', context)

def bidding(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new = Details_of_Entry(email=email, phone=phone)
        new.save()
    return render(request, 'start/bidding.html')

def blog(request):
    return render(request, 'start/blog.html')

def popup(request):
    return render(request, 'start/popup.html')

