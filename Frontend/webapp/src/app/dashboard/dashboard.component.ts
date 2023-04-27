import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
    data : any;




    constructor(
      private formBuilder: FormBuilder,
      private http: HttpClient,
      private router: Router,
      private authService: AuthService
    ) {}


    ngOnInit(): void{
      this.http.get("http://127.0.0.1:8000/apis/users/profile/view/").subscribe((response)=>{
      this.data=response;
      console.log(this.data);
    
    });
      
}}
