import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators,FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';
import { Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  Username: string;
  password: string;
  Email: string;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
      
  }

  Register() {
    let body={username:this.Username,password:this.password,email:this.Email};
    console.log(body);
    this.http.post("http://127.0.0.1:8000/apis/users/auth/register/", body).pipe(map((response:any)=>response.token)).subscribe(token=>{
    this.authService.setToken(token);
    console.log(token);
    if(token != null){
      alert('User registered sucessfully');
      window.location.reload();
  
      
      }
    //this.router.navigate(['/dashboard']);
    //this.http.get("http://127.0.0.1:8000/apis/users/profile/view/").subscribe((response)=>{console.log(response)});
    },error=>{  alert('failed to register user')
    window.location.reload();;});
    
  
}

  @Input() error: string | null;

  @Output() submitEM = new EventEmitter(); 

  register(){}

}
