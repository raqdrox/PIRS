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
  //token : any;
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
    //this.token=null;
    let body={username:this.email,password:this.password};
    console.log(body);
    this.http.post("http://localhost:8000/apis/users/auth/login/", body).pipe(map((response:any)=>response.token)).subscribe(token=>{
    this.authService.setToken(token);
    
    if(token != null){
    alert('Login sucessfull');

    this.router.navigate(['/dashboard']);
    }
    else{
      alert('invalid credentials');
    }
  
    
    },error=>{});
    
  
}



  @Input() error: string | null;

  @Output() submitEM = new EventEmitter(); 
}


