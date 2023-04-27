import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { UpdateprofileComponent } from './updateprofile/updateprofile.component';
import { AddpatientComponent } from './addpatient/addpatient.component';
import { ViewpatientComponent } from './viewpatient/viewpatient.component';
import { LogoutComponent } from './logout/logout.component';
import { UpdatepatientComponent } from './updatepatient/updatepatient.component';




const routes: Routes = [
  {path:'',component:LoginComponent},
  {path:'dashboard',component:DashboardComponent},
  {path:'register',component:RegisterComponent},
  {path:'updateprofile',component:UpdateprofileComponent},
  {path:'addpatient',component:AddpatientComponent},
  {path:'viewpatient',component:ViewpatientComponent},
  {path:'updatepatient',component:UpdatepatientComponent},
  {path:'logout',component:LogoutComponent}

  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 

  Username: string;
  password: string;
  Email: string;
}
