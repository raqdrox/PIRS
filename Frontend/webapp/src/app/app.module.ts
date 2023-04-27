import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormBuilder, FormGroup, Validators ,ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthInterceptor } from './auth.interceptor';
import { AuthService } from './token-service.service';
import { RegisterComponent } from './register/register.component';
import { FormsModule } from '@angular/forms';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {NoopAnimationsModule} from '@angular/platform-browser/animations';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { UpdateprofileComponent } from './updateprofile/updateprofile.component';
import { AddpatientComponent } from './addpatient/addpatient.component';
import { ViewpatientComponent } from './viewpatient/viewpatient.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';
import {MatTableModule} from '@angular/material/table';
import { UpdatepatientComponent } from './updatepatient/updatepatient.component';
import { LogoutComponent } from './logout/logout.component';





@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    RegisterComponent,
    UpdateprofileComponent,
    AddpatientComponent,
    ViewpatientComponent,
    UpdatepatientComponent,
    LogoutComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,MatTableModule,
    HttpClientModule,MatCardModule,MatInputModule,MatButtonModule,FormsModule,BrowserAnimationsModule,FontAwesomeModule,MatFormFieldModule,MatSelectModule
  ],
  providers: [{provide:HTTP_INTERCEPTORS,
                useClass:AuthInterceptor,
                multi:true},AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
