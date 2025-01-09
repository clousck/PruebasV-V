import { Body, Controller, Get, Post, UnauthorizedException} from '@nestjs/common';
import { AppService } from './app.service';
import { LoginRequest } from './dto/login-request.dto';
import { LoginResponse } from './dto/login-response.dto';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Post("/good-api/login")
  goodTest(@Body() loginRequest: LoginRequest): LoginResponse {
    if (loginRequest.username === "user" && loginRequest.password === "password") {
      return new LoginResponse("good-token");
    }

    throw new UnauthorizedException();
  }

  @Post("/bad-api/login")
  badTest(@Body() LoginRequest: LoginRequest): LoginResponse {
    return new LoginResponse("good-token")
  }
}
