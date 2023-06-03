import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../token-service.service';
import { Token } from '@angular/compiler';
import { map } from 'rxjs';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {


  data:any;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private authService: AuthService
  ) {}


  ngOnInit(): void{
    this.http.post("http://127.0.0.1:8000/apis/users/auth/logout/",{}).subscribe((response)=>{
    this.data=response;
    console.log(this.data);
    alert(this.data)
    this.router.navigate(['']);
    
  
  });
    
}

}
