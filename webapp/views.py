from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from kaizntree.settings import LOW_STOCK
from .forms import CreateUserForm
from .models import InventoryItem


class CreateAccount(View):
    def get(self, request):
        form  = CreateUserForm()
        return render(request, 'login/create_account.html', {'form': form})
    
    def post(self, request):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('item-dashboard')
        
        return render(request, 'login/create_account.html', {'form': form})


class ItemDashboard(LoginRequiredMixin ,View):
    def get(self, request):
        items = InventoryItem.objects.filter(user = self.request.user.id).order_by('id')
        
        low_stock_items = InventoryItem.objects.filter(
            user=self.request.user.id,
            stock__lte=LOW_STOCK,
            stock_avail__lte=LOW_STOCK,
        ).values_list('id', flat=True)

        return render(request, 'item_dashboard/item_dashboard.html', {'items': items, 'low_stock_items': low_stock_items})
    
    
    





