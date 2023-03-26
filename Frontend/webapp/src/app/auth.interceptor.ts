import { Injectable } from '@angular/core';
import { AuthService } from './token-service.service';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private authService: AuthService) {}
  
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = this.authService.getToken();
    
    
      const authReq = request.clone({
      headers: request.headers.set('Authorization', `Token ${token}`)

    });
    return next.handle(authReq);
    
    
    
  }
}