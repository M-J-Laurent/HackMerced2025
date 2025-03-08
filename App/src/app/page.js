"use client"
 
import "./globals.css"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
 
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Textarea } from "@/components/ui/textarea"
 
const FormSchema = z.object({
  bio: z
    .string()
    .min(10, {
      message: "Bio must be at least 10 characters.",
    })
    .max(160, {
      message: "Bio must not be longer than 30 characters.",
    }),
})

export default function Home() {
  const form = useForm()

  // const form = useForm<z.infer<typeof FormSchema>>({
  //   resolver: zodResolver(FormSchema),
  // })
 
  function onSubmit(data) {
    alert(data.text);
  }



  return (
    <>
      <div className="h-screen">
          <h1 className="text-center text-4xl font-bold py-10">Charity Growth Predictor</h1>
          <div className="mx-10 my-10 w-[2xl] flex justify-center">
              <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className="w-2xl space-y-6">
                  <FormField
                    control={form.control}
                    name="text"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>What kind of Charity would you start?</FormLabel>
                        <FormControl>
                          <Textarea
                            placeholder="Tell us a little bit about yourself"
                            className="resize-none"
                            {...field}
                            style={{border: "1px solid gray"}}
                          />
                        </FormControl>
                        <FormDescription>
                          Ex: water conservation
                        </FormDescription>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <Button type="submit">Submit</Button>
                </form>
              </Form>
          </div>
      </div>
    </>
  );
}
