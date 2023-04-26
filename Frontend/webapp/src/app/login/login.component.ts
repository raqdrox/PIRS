import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';
import { Input, Output, EventEmitter } from '@angular/core';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email: string;
  password: string;
  token : any;
  loginForm: FormGroup;
  submitted = false;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit() {}
   

  // convenience getter for easy access to form fields
  

  login() {
    let body={username:this.email,password:this.password};
    console.log(body);
    this.http.post("http://127.0.0.1:8000/apis/users/auth/login/", body).pipe(map((response:any)=>response.token)).subscribe(token=>{
    this.authService.setToken(token);

    this.router.navigate(['/dashboard']);
    
    },error=>{});
    
  
}



  @Input() error: string | null;

  @Output() submitEM = new EventEmitter(); 
}


